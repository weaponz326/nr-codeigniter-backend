from django.contrib import admin

from .models import AdditionalProfile, LocationDetails, Contact


# Register your models here.

class AdditionalProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_birth', 'gender')

class LocationDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'country', 'state', 'city')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'backup_email', 'phone')

admin.site.register(AdditionalProfile, AdditionalProfileAdmin)
admin.site.register(LocationDetails, LocationDetailsAdmin)
admin.site.register(Contact, ContactAdmin)
