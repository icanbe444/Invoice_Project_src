import profile
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    FormView, 
    TemplateView, 
    DetailView, 
    UpdateView,
    RedirectView,
    DeleteView,
)
from django.urls import reverse
from invoices.forms import InvoiceForm
from positions.models import Positions
from .models import Invoice
from profiles.models import Profile
from django.views.generic import View
from django.contrib import messages
from positions.forms import PositionForm
from .mixins import InvoiceNotClosedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class InvoiceListView(ListView):
    model           = Invoice
    template_name   = "invoices/main.html" #default invoice_list.html
    paginate_by     = 4
    context_object_name = 'qs'

    def get_queryset(self):
        #profile = Profile.objects.get(user=self.request.user) #this is an alternative for get_object_or_404
        profile = get_object_or_404(Profile, user = self.request.user)
        # qs = Invoice.objects.filter(profile = profile).order_by('-created')
        #qs = Invoice.objects.all().order_by('-created')  #This is used to output all the invoices
        # return qs

        return super().get_queryset().filter(profile = profile).order_by('-created') #this is an alternative for returning qs

#this class lets user create a new form 
class InvoiceFormView(LoginRequiredMixin, FormView):
    form_class      = InvoiceForm
    template_name   = 'invoices/create.html'
    # success_url     = reverse_lazy('invoices:main') #this will return the form to main view after successfull completion of a new form
    i_instance      = None


    def get_success_url(self):
        return reverse('invoices:detail', kwargs={'pk': self.i_instance.pk})


    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

class SimpleTemplateView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'invoices/detail.html'

#this is used to replace the success_url (user is redirected here after a save)
# class SimpleTemplateView(TemplateView):
#     template_name = 'invoices/simple_template.html'


class AddPositionsFormView(LoginRequiredMixin, FormView): #this is to add positions to the invoice
    form_class      = PositionForm
    template_name   = 'invoices/detail.html'
   
    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        invoice_pk       = self.kwargs.get('pk')
        invoice_obj      = Invoice.objects.get(pk = invoice_pk)
        instance         = form.save(commit=False)
        instance.invoice = invoice_obj
        form.save()
        messages.info(self.request, f'successfully added position - {instance.title}')
        return super().form_valid(form)

    #in class based view- this method is used to pass message to the template (get_context_data)
    def get_context_data(self, **kwargs):
        context         = super().get_context_data(**kwargs)
        invoice_obj     = Invoice.objects.get(pk=self.kwargs.get('pk'))
        qs              = invoice_obj.positions
        context['obj']  = invoice_obj
        context['qs']   = qs    
        return context


#I used the function created in mixins.py here to protect user from deleting using the path
class InvoiceUpdateView(LoginRequiredMixin, InvoiceNotClosedMixin, UpdateView):
    model = Invoice
    template_name = 'invoices/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoices:main')

    #this function is used to display the alert message after update is done
    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f'Successfully updated invoice - {instance.number}')
        return super().form_valid(form)



class CloseInvoiceView(LoginRequiredMixin, RedirectView):
    pattern_name = "invoices:detail"


    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Invoice.objects.get(pk = pk)
        obj.closed = True
        obj.save()
        return super().get_redirect_url(*args, **kwargs)



#I used the function created in mixins.py here to protect user from deleting using the path
class InvoicePositionsDeleteView(LoginRequiredMixin, InvoiceNotClosedMixin, DeleteView):
    model = Positions
    template_name = 'invoices/position_confirm_delete.html'

    #/<pk>/delete/<position_pk>/
    def get_object(self):
        pk = self.kwargs.get('position_pk')
        obj = Positions.objects.get(pk = pk)
        return obj


    def get_success_url(self):
        messages.info(self.request, f'Deleted Position -{self.object.title}' )
        return reverse('invoices:detail', kwargs={'pk': self.object.invoice.id})


#imports for xhtml2pdf
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

@login_required
def invoice_pdf_view(request, **kwargs):

    pk = kwargs.get('pk')
    obj = Invoice.objects.get(pk=pk)

    logo_result = finders.find('img/logo.png')
    font_result = finders.find('fonts/Lato-Regular.ttf')
    # shows search location results
    searched_locations = finders.searched_locations
    print(searched_locations)

    template_path = 'invoices/pdf.html'
    context = {
        'object': obj,
        'static': {
            'font': font_result,
            'logo': logo_result,
        },

    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html.encode('utf-8'), dest=response, encoding='utf-8')

    # if case of error
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response