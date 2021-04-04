from django.contrib import admin
from .models import Payroll


# Register your models here.

class PayrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'payroll_name', 'payroll_status', 'month', 'year')

admin.site.register(Payroll, PayrollAdmin)
