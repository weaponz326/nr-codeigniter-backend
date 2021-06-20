from django.contrib import admin
from .models import Attendance, AttendanceSheet


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_code', 'attendance_name', 'source')

class AttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'student')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceSheet, AttendanceSheetAdmin)
