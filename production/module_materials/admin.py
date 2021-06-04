from django.contrib import admin
from .models import Material


# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'material_code', 'material_name', 'category')

admin.site.register(Material, MaterialAdmin)
