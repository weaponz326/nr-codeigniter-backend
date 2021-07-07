from django.contrib import admin
from .models import Report, ReportAssessment, ReportStudent


# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'report_code', 'report_name', 'report_date', 'clas')

class ReportAssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'report', 'assessment')

class ReportStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'report', 'student')

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportAssessment, ReportAssessmentAdmin)
admin.site.register(ReportStudent, ReportStudentAdmin)
