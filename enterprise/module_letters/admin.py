from django.contrib import admin
from .models import Received, Sent


# Register your models here.

class ReceivedAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_number', 'sender', 'date_received', 'account')

class SentAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_number', 'recipient', 'date_sent', 'account')

admin.site.register(Received, ReceivedAdmin)
admin.site.register(Sent, SentAdmin)
