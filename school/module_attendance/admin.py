from django.contrib import admin
from .models import Attendance, AttendanceStudent, AttendanceDay, AttendanceCheck


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'attendance_code', 'attendance_name', 'source')

class AttendanceStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance', 'student')

class AttendanceDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance')

class AttendanceCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_student', 'day', 'check')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceStudent, AttendanceStudentAdmin)
admin.site.register(AttendanceDay, AttendanceDayAdmin)
admin.site.register(AttendanceCheck, AttendanceCheckAdmin)
