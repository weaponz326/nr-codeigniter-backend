from rest_framework import serializers

from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
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
            'teacher_code',
            'department',
            'education',
            'grade',
        ]

# merges first name and last name
class TeacherListSerializer(serializers.ModelSerializer):
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = [
            'id', 
            'account', 
            'teacher_code',
            'teacher_name',
            'department',
        ]

    def get_teacher_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
