from django.db import models
from datetime import datetime

from django.forms import URLField

# Create your models here.
"""
This is the class for company receiving invoice
"""
class Receiver(models.Model):
    name    = models.CharField(max_length= 200)
    address = models.TextField()
    website = models.URLField(blank=True)
    created = models.DateTimeField(default=datetime.now)


    #add later:
    #logo

    def __str__(self):
        return str(self.name)