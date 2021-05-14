from rest_framework import serializers

from .models import Class, ClassSubject
from module_teachers.serializers import TeacherListSerializer


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ClassListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    class_teacher = TeacherListSerializer()

    class Meta:
        model = Class
        fields = '__all__'
        depth = 1

class ClassSubjectSerializer(serializers.ModelSerializer):   

    class Meta:
        model = ClassSubject
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClassSubjectSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1