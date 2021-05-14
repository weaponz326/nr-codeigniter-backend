from django.contrib import admin

from .models import Bill


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'bill_code', 'bill_date', 'customer_name')

admin.site.register(Bill, BillAdmin)
