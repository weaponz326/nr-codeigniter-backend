from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Manufacturing


# Register your models here.

class ManufacturingAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'manufacturing_code', 'start_date', 'manufacturing_status')

admin.site.register(Manufacturing, ManufacturingAdmin)
