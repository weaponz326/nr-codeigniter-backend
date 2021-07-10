from django.contrib import admin
from .models import Attendance, AttendanceMember, AttendanceDay, AttendanceCheck


# Register your models here.

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_code', 'attendance_name')

class AttendanceMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'member')

class AttendanceDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'day')

class AttendanceCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'attendance_member', 'day', 'check')

admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(AttendanceMember, AttendanceMemberAdmin)
admin.site.register(AttendanceDay, AttendanceDayAdmin)
admin.site.register(AttendanceCheck, AttendanceCheckAdmin)
