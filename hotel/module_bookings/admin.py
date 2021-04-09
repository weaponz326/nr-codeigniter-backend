from django.contrib import admin

from .models import Booking


# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_code', 'booking_date', 'guest_name', 'expected_arrival', 'booking_status')

admin.site.register(Booking, BookingAdmin)
