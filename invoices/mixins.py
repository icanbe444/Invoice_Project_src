from django.shortcuts import redirect
from .models import Invoice

class InvoiceNotClosedMixin:

    def dispatch(self, request, *args, **kwargs):
        obj = Invoice.objects.get(pk=kwargs.get('pk'))
        if obj.closed:
            return redirect('invoices:main')
        return super().dispatch(request, *args, **kwargs)