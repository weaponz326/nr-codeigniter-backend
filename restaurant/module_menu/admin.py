from django.contrib import admin

from .models import MenuItem


# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'item_code', 'item_name', 'price')

admin.site.register(MenuItem, MenuItemAdmin)
