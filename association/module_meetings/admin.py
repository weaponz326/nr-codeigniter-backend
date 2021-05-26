from django.contrib import admin
from .models import Meeting


# Register your models here.

class MeetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_activity', 'meeting_date', 'meeting_date', 'account')

admin.site.register(Meeting, MeetingAdmin)
