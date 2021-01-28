from django.contrib import admin
from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'payment_code', 'payment_date', 'patient', 'amount_paid', 'balance')

admin.site.register(Payment, PaymentAdmin)
