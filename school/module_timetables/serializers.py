from rest_framework import serializers

from .models import Timetable


class TimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timetable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TimetableSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1