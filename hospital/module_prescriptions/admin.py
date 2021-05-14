from django.contrib import admin
from .models import Prescription, PrescriptionDetail


# Register your models here.

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'prescription_code', 'prescription_date', 'patient')

class PrescriptionDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'prescription', 'medicine')

admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(PrescriptionDetail, PrescriptionDetailAdmin)
