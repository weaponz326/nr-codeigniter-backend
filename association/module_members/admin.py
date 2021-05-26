from django.contrib import admin
from .models import Member


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'member_code', 'phone', 'account')

admin.site.register(Member, MemberAdmin)
