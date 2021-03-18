from django.contrib import admin
from .models import Attendance


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_code', 'attendance_name', 'source')

admin.site.register(Attendance, AttendanceAdmin)
