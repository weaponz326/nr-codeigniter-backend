from django.contrib import admin

from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'order', 'payment_code', 'payment_date', 'customer_name', 'payment',)

admin.site.register(Payment, PaymentAdmin)
