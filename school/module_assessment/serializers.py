from rest_framework import serializers

from .models import Assessment
from module_terms.models import Term
from module_subjects.models import Subject


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'assessment_code', 'assessment_name', 'assessment_date']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_code', 'subject_name']

# merge assessment and subjects
class AssessmentListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = Assessment
        fields = ['id', 'subject', 'assessment_code', 'assessment_name', 'assessment_date']
