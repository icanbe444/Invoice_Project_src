from .views import (
    InvoiceListView,
    InvoiceFormView,
    InvoiceUpdateView,
    AddPositionsFormView,
    CloseInvoiceView,
    InvoicePositionsDeleteView,
    invoice_pdf_view,
)
from django.urls import path

app_name = 'invoices'
urlpatterns = [
    path('', InvoiceListView.as_view(), name = 'main'),
    path('new/', InvoiceFormView.as_view(), name = 'create'),
    # path('<pk>/', SimpleTemplateView.as_view(), name = 'simple_template'),
    path('<pk>/', AddPositionsFormView.as_view(), name = 'detail'),
    path('<pk>/close/', CloseInvoiceView.as_view(), name = 'close'),
    path('<pk>/update/', InvoiceUpdateView.as_view(), name = 'update'),
    path('<pk>/pdf/', invoice_pdf_view, name="pdfs"),
    path('<pk>/delete/<int:position_pk>/', InvoicePositionsDeleteView.as_view(), name = 'position-delete'),
]