from django.contrib import admin
from .models import Doctor


# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'account', 'doctor_code')

admin.site.register(Doctor, DoctorAdmin)
