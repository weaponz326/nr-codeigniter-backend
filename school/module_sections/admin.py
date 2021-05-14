from django.contrib import admin
from .models import Section, SectionStudents


# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name', 'teacher')

class SectionStudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'student')

admin.site.register(Section, SectionAdmin)
admin.site.register(SectionStudents, SectionStudentsAdmin)
