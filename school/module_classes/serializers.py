from rest_framework import serializers

from .models import Class, ClassSubject
from module_subjects.models import Subject


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'department', 'location']

# for insertion operations
class ClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id']

# merges class to subjects
# for retreiving

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_code', 'subject_name']

class ClassSubjectListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()

    class Meta:
        model = ClassSubject
        fields = ['id', 'subject']
