from django.contrib import admin
from .models import Report


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_code', 'report_name', 'report_date', 'clas')

admin.site.register(Report, ReportAdmin)
