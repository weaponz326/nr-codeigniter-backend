from rest_framework import serializers

from .models import Timetable
from module_terms.models import Term


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'timetable_code', 'timetable_name', 'timetable_date']
