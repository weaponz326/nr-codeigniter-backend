from django.contrib import admin
from .models import Dispensary, DispensaryDrug


# Register your models here.

class DispensaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'dispense_code', 'dispense_date', 'prescription')

class DispensaryDrugAdmin(admin.ModelAdmin):
    list_display = ('id', 'dispensary', 'drug')

admin.site.register(Dispensary, DispensaryAdmin)
admin.site.register(DispensaryDrug, DispensaryDrugAdmin)
