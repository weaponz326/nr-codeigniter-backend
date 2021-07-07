from rest_framework import serializers

from .models import Section, SectionStudent
from module_teachers.serializers import TeacherListSerializer
from module_students.serializers import StudentListSerializer

class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'

class SectionListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    teacher = TeacherListSerializer()

    class Meta:
        model = Section
        fields = '__all__'

class SectionStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'

class SectionStudentListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    student = StudentListSerializer()

    class Meta:
        model = Section
        fields = '__all__'
