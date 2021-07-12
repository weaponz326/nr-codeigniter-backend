from django.contrib import admin
from .models import Roster, Shift, Batch, WorkerPersonnel, RosterDay, RosterSheet


# Register your models here.

class RosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'roster_code', 'roster_name')

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'shift_name', 'start_time', 'end_time')

class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'batch_name', 'batch_symbol')

class WorkerPersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'worker', 'batch')

class RosterDayAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster', 'day')

class RosterSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster_day', 'shift', 'batch')

admin.site.register(Roster, RosterAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(WorkerPersonnel, WorkerPersonnelAdmin)
admin.site.register(RosterDay, RosterDayAdmin)
admin.site.register(RosterSheet, RosterSheetAdmin)
