from django.contrib import admin

from .models import ExtendedProfile


# Register your models here.

class ExtendedProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'gender', 'phone', 'country')

admin.site.register(ExtendedProfile, ExtendedProfileAdmin)
