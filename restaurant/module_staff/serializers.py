from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    
    class Meta:
        model = Staff
        fields = '__all__'

# merges first name and last name
class StaffListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    staff_name = serializers.SerializerMethodField()

    class Meta:
        model = Staff
        fields = '__all__'

    def get_staff_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
