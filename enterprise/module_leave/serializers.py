from rest_framework import serializers

from .models import Leave


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = [
            'id', 
            'leave_code',
            'date_requested',
            'leave_type',
            'from_date',
            'to_date',
            'duration',
            'reason',
            'status',
        ]

