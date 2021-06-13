from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)

    class Meta:
        model = Patient
        fields = '__all__'

# merges first name and last name
class PatientListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = '__all__'

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
