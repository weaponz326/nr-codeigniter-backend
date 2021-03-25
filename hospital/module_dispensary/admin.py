from django.contrib import admin
from .models import Dispensary, Detail


# Register your models here.

class DispensaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'dispense_code', 'dispense_date', 'prescription')

class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'dispensary', 'drug')

admin.site.register(Dispensary, DispensaryAdmin)
admin.site.register(Detail, DetailAdmin)
