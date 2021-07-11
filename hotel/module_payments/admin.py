from django.contrib import admin

from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'bill', 'payment_code', 'payment_date', 'payment')

admin.site.register(Payment, PaymentAdmin)
