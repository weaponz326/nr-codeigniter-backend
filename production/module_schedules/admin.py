from django.contrib import admin

from .models import Schedule


# Register your models here.

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'account',  'schedule_code', 'schedule_name', 'from_date')

admin.site.register(Schedule, ScheduleAdmin)
