from django.contrib import admin
from .models import Rink


# Register your models here.

class RinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'rink_date', 'rink_type')

admin.site.register(Rink, RinkAdmin)
