from django.contrib import admin
from .models import Laboratory


# Register your models here.

class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'lab_code', 'lab_type', 'lab_date', 'patient')

admin.site.register(Laboratory, LaboratoryAdmin)
