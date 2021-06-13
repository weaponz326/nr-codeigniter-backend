from django.contrib import admin

from .models import Staff


# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'account', 'staff_code', 'job')

admin.site.register(Staff, StaffAdmin)
