from rest_framework import serializers

from .models import Invoice, InvoiceItem


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'invoice_date', 'customer_name', 'customer_contact', 'due_date']
