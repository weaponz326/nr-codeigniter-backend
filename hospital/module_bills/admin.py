from django.contrib import admin
from .models import Bill, General


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'bill_code', 'bill_date', 'patient', 'admission')

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'item', 'amount')

admin.site.register(Bill, BillAdmin)
admin.site.register(General, GeneralAdmin)
