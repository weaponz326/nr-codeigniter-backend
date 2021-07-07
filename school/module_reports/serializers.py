from rest_framework import serializers

from .models import Report, ReportAssessment, ReportStudent
from module_assessment.serializers import AssessmentSheetListSerializer
from module_students.serializers import StudentListSerializer


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReportSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
            
class ReportAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportAssessment
        fields = '__all__'
        depth = 1

    def __init__(self, *args, **kwargs):
        super(ReportAssessmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ReportStudentListSerializer(serializers.ModelSerializer):

    # contains serializer method field
    student = StudentListSerializer()

    class Meta:
        model = ReportStudent
        fields = '__all__'
        depth = 1
