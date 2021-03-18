from django.contrib import admin
from .models import Assessment


# Register your models here.

class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment_code', 'assessment_name', 'assessment_date', 'subject')

admin.site.register(Assessment, AssessmentAdmin)
