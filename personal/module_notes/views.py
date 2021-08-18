from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import generics, mixins
from rest_framework.parsers import FileUploadParser

from .models import Note, NoteFile
from .serializers import NoteSerializer, NoteFileSerializer


# Create your views here.

class NoteView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Note.objects.filter(user=user)
        serializer = NoteSerializer(account, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class NoteDetailView(APIView):
    def get(self, request, pk, format=None):
        account = Note.objects.get(pk=pk)
        serializer = NoteSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = Note.objects.get(pk=pk)
        serializer = NoteSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        account = Note.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # update and get subject and body individually

# class SubjectView(APIView):  
#     def get(self, request, *args, **kwargs):
#         serializer_class = NoteSerializer
#         queryset = Note.objects.all()
#         note = queryset.get(id=request.query_params.get('note_id', None))

#         return Response({ 'subject': note.subject })

#     def put(self, request, *args, **kwargs):
#         note = Note(subject=request.data.get("subject"))
#         note.id=request.data.get("note_id")
#         note.save(update_fields=['subject'])
        
#         return Response({ 'status': True })

# class BodyView(APIView):
#     def get(self, request, *args, **kwargs):
#         serializer_class = NoteSerializer
#         queryset = Note.objects.all()
#         note = queryset.get(id=request.query_params.get('note_id', None))

#         return Response({ 'body': note.body })

#     def put(self, request, *args, **kwargs):
#         note = Note(body=request.data.get("body"))
#         note.id=request.data.get("note_id")
#         note.save(update_fields=['body'])
        
#         return Response({ 'status': True })

# file attachments

class FileView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        serializer = NoteFileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response({ 'status': True })

        # if 'file' not in request.data:
        #     raise ParseError("Empty content")
        # f = request.data['file']
        # NoteFile.file.save(f.name, f, save=True)
        # return Response({ 'status': True })

    def delete(self, request, *args, **kwargs):
        pass

        # NoteFile.file.delete(save=True)
        # return Response({ 'status': True })