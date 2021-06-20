from django.contrib import admin
from .models import Roster


# Register your models here.

class RosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'roster_code', 'roster_name', 'source')

admin.site.register(Roster, RosterAdmin)
