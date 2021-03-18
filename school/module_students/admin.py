from django.contrib import admin
from .models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id',  'account', 'student_code', 'first_name', 'last_name', 'clas')

admin.site.register(Student, StudentAdmin)
