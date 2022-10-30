from random import random
from django import forms
from django.core.exceptions import ValidationError
from .models import Invoice
from profiles.utils import generate_invoice_number



class InvoiceForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Real Completion Date')
    issue_date      = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    payment_date    = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    
    class Meta:
        model = Invoice
        fields = (
            'receiver', 
            'number', 
            'completion_date', 
            'issue_date', 
            'payment_date'
            )
        labels = {#dates cannot be changed here
                'receiver': 'Customer'
                

            }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        # if len(number) < 5:
        #     raise ValidationError('Number is too short')
        if number == "":
            number = generate_invoice_number()
        return number
        

        