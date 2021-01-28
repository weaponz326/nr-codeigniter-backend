from django.contrib import admin
from .models import Prescription, Detail


# Register your models here.

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'prescription_code', 'prescription_date', 'patient')

class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'prescription')

admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Detail, DetailAdmin)
