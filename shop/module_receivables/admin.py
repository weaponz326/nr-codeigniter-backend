from django.contrib import admin

from .models import Receivable


# Register your models here.

class ReceivableAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'receivable_code', 'receivable_code', 'customer_name', 'amount')

admin.site.register(Receivable, ReceivableAdmin)
