from rest_framework import serializers
from drf_base64.fields import Base64FileField

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)

    class Meta:
        model = Worker
        fields = '__all__'

# merges first name and last name
class WorkerListSerializer(serializers.ModelSerializer):
    photo = Base64FileField(required=False)
    worker_name = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = '__all__'

    def get_worker_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
