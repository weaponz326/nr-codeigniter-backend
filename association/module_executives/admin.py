from django.contrib import admin
from .models import Executive


# Register your models here.

class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'position', 'date_inducted')

admin.site.register(Executive, ExecutiveAdmin)
