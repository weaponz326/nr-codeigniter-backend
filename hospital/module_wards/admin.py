from django.contrib import admin
from .models import Ward, WardPatient


# Register your models here.

class WardAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'ward_number', 'ward_name')

class WardPatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'ward', 'patient', 'status')

admin.site.register(Ward, WardAdmin)
admin.site.register(WardPatient, WardPatientAdmin)
