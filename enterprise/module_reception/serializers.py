from rest_framework import serializers

from .models import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = [
            'id', 
            'visit_code',
            'visit_date',
            'visitor_name',
            'visitor_phone',
            'arrival',
            'departure',
            'purpose',
            'tag_number',
        ]

