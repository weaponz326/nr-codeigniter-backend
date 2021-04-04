from django.contrib import admin
from .models import Visitor


# Register your models here.

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'visit_code', 'visit_date', 'visitor_name', 'account')

admin.site.register(Visitor, VisitorAdmin)
