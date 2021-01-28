from django.contrib import admin
from .models import Nurse


# Register your models here.

class NurseAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'hospital', 'nurse_code', 'department')

admin.site.register(Nurse, NurseAdmin)
