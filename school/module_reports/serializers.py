from rest_framework import serializers

from .models import Report
from module_terms.models import Term
from module_classes.models import Class


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'report_code', 'report_name', 'report_date']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'department']

# merge report and subjects
class ReportListSerializer(serializers.ModelSerializer):
    clas = ClassSerializer()

    class Meta:
        model = Report
        fields = ['id', 'clas', 'report_code', 'report_name', 'report_date']
