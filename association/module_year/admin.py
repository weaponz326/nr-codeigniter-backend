from django.contrib import admin
from .models import Year


# Register your models here.

class YearAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'year_begins', 'year_ends', 'year_status')

admin.site.register(Year, YearAdmin)
