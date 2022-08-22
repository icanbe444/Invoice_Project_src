"""invoice_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import main_page
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_page)
    path('', include('invoices.urls', namespace='invoices')),
]



#THIS IS FOR MEDIA HANDLING FOLLOWING THE SETTINGS IN SETTINGS.PY
# urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#this is to change the header of the app 
admin.site.site_header = "Invoice Admin System"
admin.site.index_title = "Management"