from rest_framework import serializers

from .models import Nurse


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
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
            'nurse_code',
            'department',
            'work_status',
            'started_work',
            'ended_work',
        ]

# merges first name and last name
class NurseListSerializer(serializers.ModelSerializer):
    nurse_name = serializers.SerializerMethodField()

    class Meta:
        model = Nurse
        fields = [
            'id', 
            'nurse_name',
            'nurse_code',
            'department',
        ]

    def get_nurse_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
