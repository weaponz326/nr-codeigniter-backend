from rest_framework import serializers

from .models import Appraisal, AppraisalForm
from module_employees.serializers import EmployeeListSerializer


class AppraisalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appraisal
        fields = '__all__'

class AppraisalFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppraisalForm
        fields = '__all__'

class AppraisalFormListSerializer(serializers.ModelSerializer):

    # contains serializer method filed
    employee = EmployeeListSerializer()
    class Meta:
        model = AppraisalForm
        fields = '__all__'
