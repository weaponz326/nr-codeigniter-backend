from django.contrib import admin

from .models import ExtendedProfile


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'phone1', 'city', 'country')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
