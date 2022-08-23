import profile
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    FormView, 
    TemplateView, 
    DetailView, 
    UpdateView
)
from django.urls import reverse
from invoices.forms import InvoiceForm
from .models import Invoice
from profiles.models import Profile
from django.views.generic import View
from django.contrib import messages
# Create your views here.

class InvoiceListView(ListView):
    model           = Invoice
    template_name   = "invoices/main.html" #default invoice_list.html
    paginate_by     = 2
    context_object_name = 'qs'

    def get_queryset(self):
        #profile = Profile.objects.get(user=self.request.user) #this is an alternative for get_object_or_404
        profile = get_object_or_404(Profile, user = self.request.user)
        # qs = Invoice.objects.filter(profile = profile).order_by('-created')
        #qs = Invoice.objects.all().order_by('-created')  #This is used to output all the invoices
        # return qs

        return super().get_queryset().filter(profile = profile).order_by('-created') #this is an alternative for returning qs

#this class lets user create a new form 
class InvoiceFormView(FormView):
    form_class      = InvoiceForm
    template_name   = 'invoices/create.html'
    # success_url     = reverse_lazy('invoices:main') #this will return the form to main view after successfull completion of a new form
    i_instance      = None


    def get_success_url(self):
        return reverse('invoices:simple_template', kwargs={'pk': self.i_instance.pk})


    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

class SimpleTemplateView(DetailView):
    model = Invoice
    template_name = 'invoices/simple_template.html'

#this is used to replace the success_url (user is redirected here after a save)
# class SimpleTemplateView(TemplateView):
#     template_name = 'invoices/simple_template.html'


class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = 'invoices/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoices:main')

    #this function is used to display the alert message after update is done
    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f'Successfully updated invoice - {instance.number}')
        return super().form_valid(form)