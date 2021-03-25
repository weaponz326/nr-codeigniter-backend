from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
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
            'doctor_code',
            'department',
            'speciality',
            'work_status',
            'started_work',
            'ended_work',
        ]

# merges first name and last name
class DoctorListSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = [
            'id', 
            'doctor_name',
            'doctor_code',
            'speciality',
        ]

    def get_doctor_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
