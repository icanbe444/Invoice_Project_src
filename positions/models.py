from django.db import models
from invoices.models import Invoice

# Create your models here.

class Positions(models.Model):
    invoice     = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text= "Optional Info")
    amount      = models.DecimalField(help_text="in Nigerian N", max_digits=15, decimal_places=2)
    created     = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Invoice number:  {self.invoice.number}, position title: {self.title}"


 