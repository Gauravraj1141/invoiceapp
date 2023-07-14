from rest_framework.views import APIView
from rest_framework.response import Response
from .models import InvoiceDetail, Invoice
from .serializers import InvoiceSerializer

class GetInvoice(APIView):
    def get(self, request):
        invoices = Invoice.objects.all().prefetch_related('details')
        serializer = InvoiceSerializer(invoices, many=True)
        output = dict(zip(("Status","Message","Payload"),(200,"Successfully fetched all invoices.",serializer.data)))
        return Response(output)
    

class CreateInvoice(APIView):
    def post(self, request):
        try:
            invoice_data = request.data
            invoice = Invoice.objects.create(date=invoice_data['date'],invoice_no=invoice_data['invoice_no'],customer_name=invoice_data['customer_name'])
            for invoice_detail in invoice_data['details']:
                invoice_details = InvoiceDetail.objects.create(invoice=invoice,description=invoice_detail['description'],quantity=invoice_detail['quantity'],unit_price=invoice_detail['unit_price'],price=invoice_detail['price'])
            output = dict(zip(("Status","Message","Payload"),(200,"Successfully created new invoice.","created")))
            return Response(output)
        except Exception as Ex:
            output = dict(zip(("Status","Message","Payload"),(401,"Some error occured.",str(Ex))))
            return Response(output)

    
