from rest_framework import serializers
from .models import Note, NoteFile


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class NoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteFile
        fields = '__all__'
