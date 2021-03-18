from django.contrib import admin
from .models import Timetable


# Register your models here.

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'timetable_code', 'timetable_name', 'timetable_date')

# class TimetablePeriodAdmin(admin.ModelAdmin):
#     list_display = ('id', 'timetable', 'periods')

admin.site.register(Timetable, TimetableAdmin)
# admin.site.register(TimetablePeriod, TimetablePeriodAdmin)
