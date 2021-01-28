from django.contrib import admin
from .models import Drug


# Register your models here.

class DrugAdmin(admin.ModelAdmin):
    list_display = ('id', 'ndc_number', 'drug_name', 'remaining_quantity')

admin.site.register(Drug, DrugAdmin)
