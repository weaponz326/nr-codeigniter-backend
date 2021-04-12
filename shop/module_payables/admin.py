from django.contrib import admin

from .models import Payable


# Register your models here.

class PayableAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'payable_code', 'payable_code', 'customer_name', 'amount')

admin.site.register(Payable, PayableAdmin)
