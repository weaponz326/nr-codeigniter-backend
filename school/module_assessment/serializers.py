from rest_framework import serializers

from .models import Assessment
from module_terms.models import Term
from module_subjects.models import Subject


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

