from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
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
            'worker_code',
            'department',
            'speciality',
            'job',
        ]

# merges first name and last name
class WorkerListSerializer(serializers.ModelSerializer):
    worker_name = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = [
            'id', 
            'worker_name',
            'worker_code',
            'job',
            'department',
        ]

    def get_worker_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
