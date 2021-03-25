from django.contrib import admin
from .models import Patient


# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'account', 'clinical_number')

admin.site.register(Patient, PatientAdmin)
