from django.contrib import admin
from .models import Ledger, LedgerItem


# Register your models here.

class LedgerAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'ledger_code', 'ledger_date', 'ledger_name')

class LedgerItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'ledger', 'item_date', 'reference_number', 'credit', 'debit')

admin.site.register(Ledger, LedgerAdmin)
admin.site.register(LedgerItem, LedgerItemAdmin)
