from django.contrib import admin
from .models import Roster, Shift, Batch, DoctorsPersonnel, RosterDays, RosterSheet


# Register your models here.

class RosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'roster_code', 'roster_name', 'source')

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'shift_name', 'start_time', 'end_time')

class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'batch_name', 'batch_symbol')

class DoctorsPersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'doctor', 'batch')

class RosterDaysAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster')

class RosterSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'shift')

admin.site.register(Roster, RosterAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(DoctorsPersonnel, DoctorsPersonnelAdmin)
admin.site.register(RosterDays, RosterDaysAdmin)
admin.site.register(RosterSheet, RosterSheetAdmin)
