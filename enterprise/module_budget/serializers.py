from rest_framework import serializers

from .models import Budget, Income, Expenditure


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'budget_name', 'budget_type', 'created_at']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'budget', 'item', 'amount']

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id', 'budget', 'item', 'amount']
