from django.contrib import admin
from .models import Asset


# Register your models here.

class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'asset_code', 'asset_name', 'account', 'condition')

admin.site.register(Asset, AssetAdmin)
