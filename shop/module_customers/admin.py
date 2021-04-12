from django.contrib import admin

from .models import Customer


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'customer_code', 'customer_name', 'phone',)

admin.site.register(Customer, CustomerAdmin)
