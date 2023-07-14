from django.urls import path
from invoiceapp.views import GetInvoice, CreateInvoice

urlpatterns = [
    path('get',GetInvoice.as_view()),
    path('create',CreateInvoice.as_view())
]
