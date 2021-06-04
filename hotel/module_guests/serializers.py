from rest_framework import serializers

from .models import Guest


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class GuestListSerializer(serializers.ModelSerializer):
    guest_name = serializers.SerializerMethodField()

    class Meta:
        model = Guest
        fields = '__all__'

    def get_guest_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 
