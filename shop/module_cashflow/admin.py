from django.contrib import admin

from .models import Sheet


# Register your models here.

class SheetAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'sheet_code', 'sheet_name', 'sheet_type')

admin.site.register(Sheet, SheetAdmin)
