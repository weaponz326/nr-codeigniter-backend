from django.contrib import admin

from .models import (
    Cashflow,
    DailyInflow,
    DailyOutflow,
    WeeklyInflow,
    WeeklyOutflow,
    MonthlyInflow,
    MonthlyOutflow,
    QuarterlyInflow,
    QuarterlyOutflow
)


# Register your models here.

class CashflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'sheet_code', 'sheet_name', 'sheet_type')

class DailyInflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'inflow')

class DailyOutflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'outflow')

class WeeklyInflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'inflow')

class WeeklyOutflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'outflow')

class MonthlyInflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'inflow')

class MonthlyOutflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'outflow')

class QuarterlyInflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'inflow')

class QuarterlyOutflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'outflow')

admin.site.register(Cashflow, CashflowAdmin)
admin.site.register(DailyInflow, DailyInflowAdmin)
admin.site.register(DailyOutflow, DailyOutflowAdmin)
admin.site.register(WeeklyInflow, WeeklyInflowAdmin)
admin.site.register(WeeklyOutflow, WeeklyOutflowAdmin)
admin.site.register(MonthlyInflow, MonthlyInflowAdmin)
admin.site.register(MonthlyOutflow, MonthlyOutflowAdmin)
admin.site.register(QuarterlyInflow, QuarterlyInflowAdmin)
admin.site.register(QuarterlyOutflow, QuarterlyOutflowAdmin)
