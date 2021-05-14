from rest_framework import serializers

from .models import Dispensary, DispensaryDrug
from module_prescriptions.serializers import PrescriptionListSerializer


class DispensarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispensary
        fields = '__all__'

class DispensaryListSerializer(serializers.ModelSerializer):
    prescription = PrescriptionListSerializer()

    class Meta:
        model = Dispensary
        fields = '__all__'
        depth = 2

class DispensaryDrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispensaryDrug
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DispensaryDrugSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1