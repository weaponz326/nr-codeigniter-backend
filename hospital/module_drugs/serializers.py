from rest_framework import serializers

from .models import Drug


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = [
            'id', 
            'ndc_number',
            'drug_name',
            'generic_name',
            'category',
            'manufacturer',
            'drug_type',
            'unit_dose',
            'unit_price',
            'batch_number',
            'purchased_date',
            'initial_quantity',
            'dispensed_quantity',
            'remaining_quantity',
            'manufacturing_date',
            'expiry_date',
            'storage_location',
            'storage_bin',
            'refill_ordered',
        ]
