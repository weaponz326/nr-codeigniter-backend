from django.contrib import admin
from .models import Assessment, AssessmentSheet


# Register your models here.

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment_code', 'assessment_name', 'assessment_date', 'subject', 'clas')

class AssessmentSheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment', 'student', 'score', 'grade')

admin.site.register(Assessment, AssessmentAdmin)
admin.site.register(AssessmentSheet, AssessmentSheetAdmin)
