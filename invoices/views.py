from cProfile import Profile
import profile
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from invoices.forms import InvoiceForm
from .models import Invoice
from profiles.models import Profile
# Create your views here.

class InvoiceListView(ListView):
    model           = Invoice
    template_name   = "invoices/main.html" #default invoice_list.html
    # #paginate_by
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
    success_url     = reverse_lazy('invoices:main') #this will return the form to main view after successfull completion of a new form



    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        return super().form_valid(form)