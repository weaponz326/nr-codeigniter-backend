from django.contrib import admin
from .models import Teacher


# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id',  'account', 'teacher_code', 'first_name', 'last_name', 'department')

admin.site.register(Teacher, TeacherAdmin)
