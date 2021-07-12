from rest_framework import serializers

from .models import (
    Cashflow,
    DailyInflow,
    DailyOutflow,
    WeeklyInflow,
    WeeklyOutflow,
    MonthlyInflow,
    MonthlyOutflow,
    QuarterlyInflow,
    QuarterlyOutflow
)


class CashflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashflow
        fields = '__all__'

class DailyInflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyInflow
        fields = '__all__'

class DailyOutflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyOutflow
        fields = '__all__'

class WeeklyInflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeeklyInflow
        fields = '__all__'

class WeeklyOutflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeeklyOutflow
        fields = '__all__'

class MonthlyInflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthlyInflow
        fields = '__all__'

class MonthlyOutflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthlyOutflow
        fields = '__all__'

class QuarterlyInflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuarterlyInflow
        fields = '__all__'

class QuarterlyOutflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuarterlyOutflow
        fields = '__all__'
