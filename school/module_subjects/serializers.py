from rest_framework import serializers

from .models import Subject
from module_terms.models import Term


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_name', 'subject_code', 'department', 'description']

# merge term with subject

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'term_name']

class SubjectListSerializer(serializers.ModelSerializer):
    term = TermSerializer()

    class Meta:
        model = Subject
        fields = ['id', 'term', 'subject_name', 'subject_code']

