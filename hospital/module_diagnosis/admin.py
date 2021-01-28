from django.contrib import admin
from .models import Diagnosis


# Register your models here.

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'diagnosis_code', 'diagnosis_date', 'patient')

admin.site.register(Diagnosis, DiagnosisAdmin)
