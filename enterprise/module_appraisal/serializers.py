from rest_framework import serializers

from .models import Appraisal
from module_employees.serializers import EmployeeListSerializer


class AppraisalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appraisal
        fields = '__all__'

class AppraisalListSerializer(serializers.ModelSerializer):
    # contains serializer method filed
    employee = EmployeeListSerializer()

    class Meta:
        model = Appraisal
        fields = '__all__'
        depth = 1