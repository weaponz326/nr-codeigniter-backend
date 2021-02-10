from django.contrib import admin
from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'payment_code', 'payment_date', 'bill', 'amount_paid', 'balance')

admin.site.register(Payment, PaymentAdmin)
