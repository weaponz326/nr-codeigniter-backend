from django.contrib import admin

from .models import Room


# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_number', 'room_type', 'account', 'rate', 'room_status')

admin.site.register(Room, RoomAdmin)
