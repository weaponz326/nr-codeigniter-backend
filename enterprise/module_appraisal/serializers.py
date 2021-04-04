from rest_framework import serializers

from .models import Appraisal


class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = ['id', 'account', 'appraisal_code', 'start_date', 'end_date', 'supervisor', 'description']
