from django.contrib import admin
from .models import Payment


# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_code', 'payment_date', 'fee', 'student', 'amount_paid')

admin.site.register(Payment, PaymentAdmin)
