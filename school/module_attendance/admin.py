from django.contrib import admin
from .models import Attendance, AttendanceSheet, AttendanceDay


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'attendance_code', 'attendance_name', 'source')

class AttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance', 'student')

class AttendanceDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceSheet, AttendanceSheetAdmin)
admin.site.register(AttendanceDay, AttendanceDayAdmin)
