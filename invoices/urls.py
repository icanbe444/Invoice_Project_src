from .views import (
    InvoiceListView,
    InvoiceFormView,
    SimpleTemplateView
)
from django.urls import path

app_name = 'invoices'
urlpatterns = [
    path('', InvoiceListView.as_view(), name = 'main'),
    path('new/', InvoiceFormView.as_view(), name = 'create'),
    path('<pk>/', SimpleTemplateView.as_view(), name = 'simple-template'),
]