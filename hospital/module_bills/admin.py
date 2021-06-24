from django.contrib import admin
from .models import (
    Bill, 
    General,
    AppointmentCharge,
    LaboratoryCharge,
    DispensaryCharge,
    WardCharge
)


# Register your models here.

class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'bill_code', 'bill_date', 'patient', 'admission')

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'item', 'amount')

class AppointmentChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'appointment', 'amount')

class LaboratoryChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'lab', 'amount')

class DispensaryChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'dispensary', 'amount')

class WardChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill', 'ward', 'amount')

admin.site.register(Bill, BillAdmin)
admin.site.register(General, GeneralAdmin)
admin.site.register(AppointmentCharge, AppointmentChargeAdmin)
admin.site.register(LaboratoryCharge, LaboratoryChargeAdmin)
admin.site.register(DispensaryCharge, DispensaryChargeAdmin)
admin.site.register(WardCharge, WardChargeAdmin)
