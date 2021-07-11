from django.contrib import admin

from .models import Checkin


# Register your models here.

class CheckinAdmin(admin.ModelAdmin):
    list_display = ('id', 'checkin_code', 'booking', 'room', 'checkin_date', 'checkout_date', 'account')

admin.site.register(Checkin, CheckinAdmin)
