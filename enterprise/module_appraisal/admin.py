from django.contrib import admin
from .models import Appraisal


# Register your models here.

class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('id', 'appraisal_code', 'start_date', 'account')

admin.site.register(Appraisal, AppraisalAdmin)
