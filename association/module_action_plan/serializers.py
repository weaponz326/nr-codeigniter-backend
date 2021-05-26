from rest_framework import serializers
from .models import Plan, Step


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StepSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
                