from django.contrib import admin

from .models import Housekeeping, Checklist


# Register your models here.

class HousekeepingAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'housekeeping_code', 'housekeeping_date', 'room')

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('id', 'housekeeping', 'item_number', 'item_description', 'status')

admin.site.register(Housekeeping, HousekeepingAdmin)
admin.site.register(Checklist, ChecklistAdmin)
