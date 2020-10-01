from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_of_birth', 'gender')

admin.site.register(Profile, ProfileAdmin)
