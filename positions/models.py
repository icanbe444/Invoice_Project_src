from django.db import models
from invoices.models import Invoice

# Create your models here.

class Positions(models.Model):
    invoice     = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True, help_text= "Optional Info")
    amount      = models.FloatField(help_text="in US $")
    created     = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Invoice number:  {self.invoice.number}, position title: {self.title}"
 