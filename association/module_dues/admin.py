from django.contrib import admin
from .models import Dues, DuesPayment


# Register your models here.

class DuesAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'dues_code', 'dues_name', 'dues_date')

class DuesPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'dues', 'payment_date', 'member', 'amount')

admin.site.register(Dues, DuesAdmin)
admin.site.register(DuesPayment, DuesPaymentAdmin)
