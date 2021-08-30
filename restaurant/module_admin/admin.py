from django.contrib import admin
from .models import User, Access, Invitation

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'personal_id', 'user_level')

class AccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'admin_access', 'portal_access', 'settings_access')

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('account', 'personal_id', 'invitation_status', 'date_sent')

admin.site.register(User, UserAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(Invitation, InvitationAdmin)
