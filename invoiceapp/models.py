from django.db import models


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True, editable=False)
    date = models.DateField()
    invoice_no = models.CharField(max_length=100, unique=True, null=True, blank=True, default=None)
    customer_name = models.CharField(max_length=100)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="details")
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)