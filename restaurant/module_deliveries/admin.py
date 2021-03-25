from django.contrib import admin

from .models import Delivery


# Register your models here.

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'delivery_code', 'delivery_date', 'order', 'delivery_status')

admin.site.register(Delivery, DeliveryAdmin)
