from django.contrib import admin

from .models import Customer


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'customer_code', 'first_name', 'last_name')

admin.site.register(Customer, CustomerAdmin)
