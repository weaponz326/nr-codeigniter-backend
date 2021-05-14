from django.contrib import admin
from .models import Fee, FeesItem


# Register your models here.

class FeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'fees_code', 'fees_date')

class FeesItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'fee', 'item', 'amount')

admin.site.register(Fee, FeeAdmin)
admin.site.register(FeesItem, FeesItemAdmin)
