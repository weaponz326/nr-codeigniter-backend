from rest_framework import serializers

from .models import Term


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ['id', 'term_name', 'term_begins', 'term_ends', 'academic_year', 'term_status']
