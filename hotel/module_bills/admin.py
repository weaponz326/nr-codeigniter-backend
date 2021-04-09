from django.contrib import admin

from .models import Bill, RoomBill, ServiceBill


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'bill_code', 'bill_date', 'guest')

class RoomBillAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'number_nights', 'amount')

class ServiceBillAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'amount')

admin.site.register(Bill, BillAdmin)
admin.site.register(RoomBill, RoomBillAdmin)
admin.site.register(ServiceBill, ServiceBillAdmin)
