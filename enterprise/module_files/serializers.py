from rest_framework import serializers

from .models import Folder, File


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['id', 'folder_number', 'folder_name', 'date_created', 'last_updated']

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file_number', 'file_name', 'date_created']
