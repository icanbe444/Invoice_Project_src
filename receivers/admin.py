from pyexpat import model
from venv import create
from django.contrib import admin

from receivers.models import Receiver
from import_export import resources
from import_export.admin import ExportActionMixin
# Register your models here.

class RecieverResource(resources.ModelResource):
    class Meta:
        model= Receiver
        fields = ('id', 'name', 'address', 'website', 'created')
        #to change the export order 
        exporp_order = ('website', 'created', 'address', 'name', 'id')

class ReceiverAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = RecieverResource
    



admin.site.register(Receiver, ReceiverAdmin)

