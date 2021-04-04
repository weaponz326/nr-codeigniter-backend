from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Folder, File
from accounts.models import Profile
from .serializers import FolderSerializer, FileSerializer


# Create your views here.

# folders

class FolderView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = FolderSerializer
        queryset = Folder.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            folder = Folder(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                folder_number=request.data.get("folder_number"),
                folder_name=request.data.get("folder_name"),
            )
            folder.save()
            latest_folder = Folder.objects.latest("id")

            return Response({
                'status': True,
                'folder_id': latest_folder.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class FolderListView(generics.ListAPIView):
    serializer_class = FolderSerializer

    def get_queryset(self):
        queryset = Folder.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class FolderDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------
# files

class FileView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = FileSerializer
        queryset = File.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = File(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                file_number=request.data.get("file_number"),
                file_name=request.data.get("file_name"),
            )
            file.save()
            latest_file = File.objects.latest("id")

            return Response({
                'status': True,
                'file_id': latest_file.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class FileDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
