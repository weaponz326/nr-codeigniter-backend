from django.contrib import admin
from .models import Attendance, AttendanceSheet, AttendanceDay


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_code', 'attendance_name')

class AttendanceSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'member')

class AttendanceDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'day')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceSheet, AttendanceSheetAdmin)
admin.site.register(AttendanceDay, AttendanceDayAdmin)
