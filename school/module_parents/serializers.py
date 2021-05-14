from rest_framework import serializers

from .models import Parent, ParentWard
from module_students.serializers import StudentListSerializer


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

# merges first name and last name
class ParentListSerializer(serializers.ModelSerializer):
    parent_name = serializers.SerializerMethodField()

    class Meta:
        model = Parent
        fields = '__all__'

    def get_parent_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name) 


class ParentWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentWard
        fields = '__all__'

class ParentWardListSerializer(serializers.ModelSerializer):
    # contains serializer method field
    ward = StudentListSerializer()

    class Meta:
        model = ParentWard
        fields = '__all__'
