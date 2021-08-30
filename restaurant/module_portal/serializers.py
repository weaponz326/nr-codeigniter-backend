from rest_framework import serializers

from .models import Rink
from accounts.models import Profile

class RinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rink
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RinkSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
