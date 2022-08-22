from django.contrib import admin
from .models import Positions
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
# Register your models here.

#this class is used for invoice export 
class PositionsResource(resources.ModelResource):
    invoice     = Field()
    description = Field()
   
    class Meta:
        model   = Positions
        fields  = ('id', 'invoice','title', 'description', 'created',  'amount')


    def dehydrate_invoice(self, obj):
        return obj.invoice.number



    def dehydrate_description(self, obj):
        if obj.description == "":
            return "-"
        return obj.description

class PositionsAdmin(ExportActionMixin,  admin.ModelAdmin):
    resource_class = PositionsResource





admin.site.register(Positions, PositionsAdmin)
