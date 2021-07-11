from django.contrib import admin

from .models import Booking, BookedRoom


# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_code', 'booking_date', 'guest_name', 'expected_arrival', 'booking_status')

class BookedRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'room_type', 'persons_number')

admin.site.register(Booking, BookingAdmin)
admin.site.register(BookedRoom, BookedRoomAdmin)
