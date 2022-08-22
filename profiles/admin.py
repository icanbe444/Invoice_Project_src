from attr import fields
from django.contrib import admin
from .models import Profile
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
# Register your models here.




class ProfileResource(resources.ModelResource):
    user = Field()
    class Meta:
        model  = Profile
        fields = ('id','user', 'account_number', 'company_name', 'company_info', 'created','updated' )


    def dehydrate_user(self, obj):
        return obj.user.username

class ProfileAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ProfileResource




admin.site.register(Profile, ProfileAdmin)
