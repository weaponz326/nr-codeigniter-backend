from rest_framework import serializers

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
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
            'staff_code',
            'department',
            'job',
            'work_status',
            'started_work',
            'ended_work',
        ]

# merges first name and last name
class StaffListSerializer(serializers.ModelSerializer):
    staff_name = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = [
            'id', 
            'account', 
            'staff_code',
            'staff_name',
            'department',
            'job',
        ]

    def get_staff_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
