from turtle import update
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


from .utils import generate_account_number
from jsonschema import ValidationError

from profiles.utils import generate_account_number
# Create your models here.
'''
Class for the owner of the invoice
'''
class Profile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number      = models.CharField(max_length= 10, blank= True)
    company_name        = models.CharField(max_length= 220)
    company_info        = models.TextField()
    created             = models.DateTimeField(auto_now= True)
    update              = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(default= 'images/silihouette.jpeg')
    company_logo = models.ImageField(default= 'images/logo.png')


    def __str__(self):
        return f"Profile of the user: {self.user.username}"

    """this function will create the account number if user didnot supply one. if account number is empty, 
        it will open the utils.py file and call the generate_account_number function
    
    """
    def save(self, *args, **kwargs):
        if self.account_number == "":
            self.account_number = generate_account_number()
        return super().save(*args, **kwargs)

        


   