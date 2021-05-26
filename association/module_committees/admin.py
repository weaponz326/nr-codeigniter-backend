from django.contrib import admin
from .models import Committee, CommitteeMember


# Register your models here.

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee_name', 'date_formed', 'committee_status')

class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee', 'member')

admin.site.register(Committee, CommitteeAdmin)
admin.site.register(CommitteeMember, CommitteeMemberAdmin)
