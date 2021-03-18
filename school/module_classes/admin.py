from django.contrib import admin
from .models import Class, ClassSubject


# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_name', 'department')

class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'clas', 'subject')

admin.site.register(Class, ClassAdmin)
admin.site.register(ClassSubject, ClassSubjectAdmin)
