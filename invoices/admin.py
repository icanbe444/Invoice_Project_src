import profile
from pyexpat import model
from turtle import position
from django.contrib import admin
from pyrsistent import field
from invoices.models import Invoice, Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin
# Register your models here.


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id', 'name')


#this class is used for tag export 
class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource


#this class is used for invoice export 
class InvoiceResource(resources.ModelResource):
    profile     = Field()
    reciever    = Field()
    created     = Field()
    closed      = Field()
    positions   = Field()
    total_amount= Field()
    
    class Meta:
        model   = Invoice
        fields  = ('id', 'profile','receiver', 'number', 'completion_date', 'issue_date', 'payment_date', 'created', 'closed', 'positions', 'total_amount')


    def dehydrate_profile(self, obj):
        return obj.profile.user.username

    def dehydrate_receiver(self, obj):
        return obj.receiver.name

    def dehydrate_created(self, obj):
        #date only
        return obj.created.strftime("%d-%m-%y")

    def dehydrate_closed(self, obj):
        if obj.closed == True:
            return "True"
        else:
            return "False"


    def dehydrate_positions(self, obj):
        positions_list = [x.title for x in obj.positions]
        positions_str = ",".join(positions_list)
        return positions_str


    def dehydrate_total_amount(self, obj):
        return obj.total_amount

    
#This is for the export of invoices to appear in the admin page
class InvoiceAdmin(ExportActionMixin,  admin.ModelAdmin):
    resource_class = InvoiceResource



admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Tag, TagAdmin)