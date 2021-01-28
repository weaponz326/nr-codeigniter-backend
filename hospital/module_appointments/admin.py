from django.contrib import admin
from .models import Appointment


# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'consultant', 'hospital', 'appointment_code')

admin.site.register(Appointment, AppointmentAdmin)
