from django.contrib import admin

from .models import ExtendedProfile, Subscription


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'phone1', 'city', 'country')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'subscription', 'plan')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
