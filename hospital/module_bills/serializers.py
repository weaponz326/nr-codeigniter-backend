from rest_framework import serializers

from .models import (
    Bill, 
    General, 
    AppointmentCharge, 
    LaboratoryCharge, 
    DispensaryCharge, 
    WardCharge
)
from module_patients.serializers import PatientListSerializer


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'

class BillListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    patient = PatientListSerializer()

    class Meta:
        model = Bill
        fields = '__all__'
        depth = 1

# bill general items

class GeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = General
        fields = '__all__'

# bill extra charges
class AppointmentChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppointmentCharge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppointmentChargeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class LaboratoryChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LaboratoryCharge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LaboratoryChargeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class DispensaryChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispensaryCharge
        fields = '__all__'    

    def __init__(self, *args, **kwargs):
        super(DispensaryChargeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1            

class WardChargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = WardCharge
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WardChargeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1