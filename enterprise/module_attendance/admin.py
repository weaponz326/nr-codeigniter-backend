from django.contrib import admin
from .models import Attendance


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'attendance_code', 'attendance_name', 'year')

admin.site.register(Attendance, AttendanceAdmin)
