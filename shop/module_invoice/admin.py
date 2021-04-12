from django.contrib import admin

from .models import Invoice, InvoiceItem


# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'invoice_number', 'invoice_date', 'customer_name', 'due_date')

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'product', 'quantity', 'total_price')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
