from django.contrib import admin
from .models import Subject


# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_code', 'subject_name', 'department')

admin.site.register(Subject, SubjectAdmin)
