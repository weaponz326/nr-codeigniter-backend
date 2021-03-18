from rest_framework import serializers

from .models import Student
from module_classes.models import Class


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id', 
            'first_name',
            'last_name',
            'sex',
            'date_of_birth',
            'nationality',
            'religion',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
            'student_code',
            'admission_date',
            'previous_school',
        ]

# merge student with class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = [
            'id', 
            'class_name',
        ]

# combine first name and last name
class StudentListSerializer(serializers.ModelSerializer):
    clas = ClassSerializer()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id', 
            'account', 
            'student_code',
            'student_name',
            'clas',
        ]

    def get_student_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
