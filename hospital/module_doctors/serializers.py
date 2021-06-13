from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    class Meta:
        model = Doctor
        fields = '__all__'

# merges first name and last name
class DoctorListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    doctor_name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = '__all__'

    def get_doctor_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
