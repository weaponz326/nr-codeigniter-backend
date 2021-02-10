from django.contrib import admin

from .models import Bill


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'bill_code', 'bill_date', 'customer_name', 'bill_type')

admin.site.register(Bill, BillAdmin)
