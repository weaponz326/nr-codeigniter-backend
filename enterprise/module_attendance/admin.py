from django.contrib import admin
from .models import Attendance, AttendanceEmployee, AttendanceDay, AttendanceCheck


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'attendance_code', 'attendance_name')

class AttendanceEmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance', 'employee')

class AttendanceDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance', 'day')

class AttendanceCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_employee', 'day', 'check')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceEmployee, AttendanceEmployeeAdmin)
admin.site.register(AttendanceDay, AttendanceDayAdmin)
admin.site.register(AttendanceCheck, AttendanceCheckAdmin)
