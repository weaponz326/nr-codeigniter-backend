from django.contrib import admin
from .models import Leave


# Register your models here.

class LeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'leave_code', 'account', 'status')

admin.site.register(Leave, LeaveAdmin)
