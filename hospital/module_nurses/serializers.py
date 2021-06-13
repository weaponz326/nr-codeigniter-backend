from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Nurse


class NurseSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)

    class Meta:
        model = Nurse
        fields = '__all__'

# merges first name and last name
class NurseListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    nurse_name = serializers.SerializerMethodField()

    class Meta:
        model = Nurse
        fields = '__all__'

    def get_nurse_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
