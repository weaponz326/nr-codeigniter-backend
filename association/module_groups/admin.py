from django.contrib import admin
from .models import Group, GroupMember


# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name')

class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'member')

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupMember, GroupMemberAdmin)
