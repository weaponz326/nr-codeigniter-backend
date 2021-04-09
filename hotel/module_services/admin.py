from django.contrib import admin

from .models import Service, ServiceItem


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_code', 'service_type', 'service_date', 'account',)

class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'item_date', 'amount')

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
