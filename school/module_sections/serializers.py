from rest_framework import serializers

from .models import Section, SectionStudents
from module_teachers.serializers import TeacherListSerializer

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

# class SectionStudentsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Section
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(SectionStudentsSerializer, self).__init__(*args, **kwargs)
#         request = self.context.get('request')
#         if request and (request.method == 'POST' or request.method == 'PUT'):
#             self.Meta.depth = 0
#         else:
#             self.Meta.depth = 1            