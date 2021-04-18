from rest_framework import serializers

from .models import Contractor


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = [
            'id', 
            'contractor_name',
            'category',
            'phone',
            'email',
            'address',
            'country',
            'state',
            'city',
            'post_code',
            'website',
            'primary_contract',
            'project_name',
            'contract_type',
            'work_description',
            'contract_status',
            'work_start_date',
            'work_end_date',
        ]
