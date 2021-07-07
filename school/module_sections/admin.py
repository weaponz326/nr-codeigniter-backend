from django.contrib import admin
from .models import Section, SectionStudent


# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_name', 'teacher')

class SectionStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'student')

admin.site.register(Section, SectionAdmin)
admin.site.register(SectionStudent, SectionStudentAdmin)
