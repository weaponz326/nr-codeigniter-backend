from django.contrib import admin
from .models import Parent, ParentWard


# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_code', 'first_name', 'last_name', 'account')

class ParentWardAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'ward')

admin.site.register(Parent, ParentAdmin)
admin.site.register(ParentWard, ParentWardAdmin)
