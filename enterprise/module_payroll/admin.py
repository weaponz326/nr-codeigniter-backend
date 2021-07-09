from django.contrib import admin
from .models import Payroll, PayrollSheet


# Register your models here.

class PayrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'payroll_name', 'payroll_status', 'month', 'year')

class PayrollSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'payroll', 'employee', 'salary')

admin.site.register(Payroll, PayrollAdmin)
admin.site.register(PayrollSheet, PayrollSheetAdmin)
