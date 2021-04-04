from django.contrib import admin
from .models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'account', 'employee_code', 'department')

admin.site.register(Employee, EmployeeAdmin)
