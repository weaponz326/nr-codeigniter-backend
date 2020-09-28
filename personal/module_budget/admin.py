from django.contrib import admin
from .models import Budget, Income, Expenditure

# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'budget_name', 'budget_type', 'created_at')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'budget', 'item', 'amount')

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('id', 'budget', 'item', 'amount')

admin.site.register(Budget, BudgetAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expenditure, ExpenditureAdmin)
