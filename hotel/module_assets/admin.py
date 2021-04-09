from django.contrib import admin

from .models import Asset


# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'asset_code', 'asset_name', 'asset_type', 'location', 'condition')

admin.site.register(Asset, AssetAdmin)
