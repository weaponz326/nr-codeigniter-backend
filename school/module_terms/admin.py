from django.contrib import admin
from .models import Term


# Register your models here.

class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'term_name', 'academic_year', 'term_status')

admin.site.register(Term, TermAdmin)
