from django.contrib import admin

from .models import Roster


# Register your models here.

class RosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'account',  'roster_code', 'roster_name', 'from_date')

admin.site.register(Roster, RosterAdmin)
