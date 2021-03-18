from rest_framework import serializers

from .models import Parent, ParentWard
from module_students.models import Student
from module_classes.models import Class


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = [
            'id', 
            'parent_code', 
            'first_name',
            'last_name',
            'sex',
            'nationality',
            'religion',
            'occupation',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
        ]

# merges first name and last name
class ParentListSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()

    class Meta:
        model = Parent
        fields = ['id', 'account', 'parent_code', 'parent_name', 'phone']

    def get_parent_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

# students serializer
# all students in a school

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'student_code']

# merge student with class
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name']

# combine first name and last name
class StudentListSerializer(serializers.ModelSerializer):
    clas = ClassSerializer()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'account', 'student_code', 'student_name', 'clas']

    def get_student_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 

# parent's wards
# only wards belonging to a parent

class ParentWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentWard
        fields = ['id']

# merge student - class combo with parent

class ParentWardListSerializer(serializers.ModelSerializer):
    ward = StudentListSerializer()

    class Meta:
        model = ParentWard
        fields = ['id', 'ward']

