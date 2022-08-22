from django import forms
from .models import Invoice



class InvoiceForm(forms.ModelForm):
    completion_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
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