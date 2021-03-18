from django.contrib import admin
from .models import User, Access, Activity

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'hospital', 'personal_id', 'is_admin')

class AccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'admin_access', 'portal_access', 'settings_access')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'activity_module', 'description')

admin.site.register(User, UserAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(Activity, ActivityAdmin)
