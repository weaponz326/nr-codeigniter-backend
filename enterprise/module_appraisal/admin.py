from django.contrib import admin
from .models import Appraisal, AppraisalForm


# Register your models here.

class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('id', 'appraisal_code', 'appraisal_name', 'start_date', 'account')

class AppraisalFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'appraisal', 'employee')

admin.site.register(Appraisal, AppraisalAdmin)
admin.site.register(AppraisalForm, AppraisalFormAdmin)
