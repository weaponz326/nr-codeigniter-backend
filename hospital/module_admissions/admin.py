from django.contrib import admin
from .models import Admission


# Register your models here.

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'admission_code', 'admission_date', 'account', 'patient', 'admission_status')

admin.site.register(Admission, AdmissionAdmin)
