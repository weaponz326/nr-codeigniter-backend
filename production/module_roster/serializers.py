from rest_framework import serializers

from .models import (
    Roster,
    RosterSheet, 
    Shift, 
    Batch, 
    WorkerPersonnel,
    RosterDay
)
from module_workers.serializers import WorkerListSerializer

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = '__all__'
        
class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
                        
class WorkerPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerPersonnel
        fields = '__all__'

class WorkerPersonnelListSerializer(serializers.ModelSerializer):
    # contain serializer menthod fields
    worker = WorkerListSerializer()

    class Meta:
        model = WorkerPersonnel
        fields = '__all__'
        depth = 1

class RosterDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterDay
        fields = '__all__'

class RosterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterSheet
        fields = '__all__'
        depth = 1
        