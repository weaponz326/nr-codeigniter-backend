from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    
    class Meta:
        model = Student
        fields = '__all__'

# combine first name and last name
class StudentListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

    def get_student_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
