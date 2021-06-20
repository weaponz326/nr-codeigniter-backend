from django.contrib import admin
from .models import Timetable, TimetablePeriod, TimetableClass


# Register your models here.

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'timetable_code', 'timetable_name', 'timetable_date')

class TimetablePeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'timetable', 'period', 'period_start', 'period_end')

class TimetableClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'timetable', 'clas')

admin.site.register(Timetable, TimetableAdmin)
admin.site.register(TimetablePeriod, TimetablePeriodAdmin)
admin.site.register(TimetableClass, TimetableClassAdmin)
