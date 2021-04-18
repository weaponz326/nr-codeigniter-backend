from django.contrib import admin
from .models import Contractor


# Register your models here.

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'contractor_name', 'category', 'primary_contract', 'contract_status')

admin.site.register(Contractor, ContractorAdmin)
