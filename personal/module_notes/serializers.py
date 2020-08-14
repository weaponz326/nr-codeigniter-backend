from rest_framework import serializers
from .models import Note, NoteFile


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'user', 'subject', 'body', 'created_at', 'updated_at']

class NoteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteFile
        fields = ['note', 'file']
