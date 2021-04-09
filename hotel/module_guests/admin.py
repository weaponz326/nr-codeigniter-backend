from django.contrib import admin

from .models import Guest


# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'first_name', 'last_name', 'sex', 'phone')

admin.site.register(Guest, GuestAdmin)
