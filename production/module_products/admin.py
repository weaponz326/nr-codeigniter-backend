from django.contrib import admin

from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'product_code', 'product_name', 'version')

admin.site.register(Product, ProductAdmin)
