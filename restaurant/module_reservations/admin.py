from django.contrib import admin

from .models import Reservation


# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'reservation_code', 'reservation_date', 'customer_name', 'reservation_status')

admin.site.register(Reservation, ReservationAdmin)
