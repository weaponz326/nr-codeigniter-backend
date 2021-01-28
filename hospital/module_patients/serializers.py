from rest_framework import serializers

from .models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 
            'hospital', 
            'first_name',
            'last_name',
            'sex',
            'date_of_birth',
            'nationality',
            'religion',
            'occupation',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
            'clinical_number',
            'insurance_type',
            'insurance_number'
        ]

# merges first name and last name
class PatientListSerializer(serializers.ModelSerializer):
    patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            'id', 
            'hospital', 
            'patient_name',
            'sex',
            'phone',
            'clinical_number'
        ]

    def get_patient_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
