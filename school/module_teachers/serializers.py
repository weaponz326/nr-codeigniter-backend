from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)

    class Meta:
        model = Teacher
        fields = '__all__'

# merges first name and last name
class TeacherListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = '__all__'
        depth = 1

    def get_teacher_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
