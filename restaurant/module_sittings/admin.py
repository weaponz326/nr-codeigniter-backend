from django.contrib import admin

from .models import Sitting


# Register your models here.

class SittingAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'sitting_code', 'sitting_date', 'customer_name')

admin.site.register(Sitting, SittingAdmin)
