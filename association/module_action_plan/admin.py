from django.contrib import admin
from .models import Plan, Step

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'plan_name', 'start_date', 'end_date', 'facilitator')

class StepAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan', 'step')

admin.site.register(Plan, PlanAdmin)
admin.site.register(Step, StepAdmin)
