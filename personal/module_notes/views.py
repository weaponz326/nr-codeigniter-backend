from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Note, NoteFile
from .serializers import NoteSerializer, NoteFileSerializer

# Create your views here.

# create, update and get subject and body individually

class SubjectView(APIView):  
    def get(self, request, *args, **kwargs):
        serializer_class = NoteSerializer
        queryset = Note.objects.all()
        note = queryset.get(id=request.query_params.get('note_id', None))

        return Response({ 'subject': note.subject })

    def post(self, request, *args, **kwargs):
        note = Note(
            user=User.objects.get(id=request.data.get("user")),
            subject=request.data.get("subject")
        )
        note.save()
        latest_note = Note.objects.latest("id")
        
        return Response({
            'status': True,
            'note_id': latest_note.id
        })

    def put(self, request, *args, **kwargs):
        note = Note(subject=request.data.get("subject"))
        note.id=request.data.get("note_id")
        note.save(update_fields=['subject'])
        
        return Response({ 'status': True })

class BodyView(APIView):
    def get(self, request, *args, **kwargs):
        serializer_class = NoteSerializer
        queryset = Note.objects.all()
        note = queryset.get(id=request.query_params.get('note_id', None))

        return Response({ 'body': note.body })

    def post(self, request, *args, **kwargs):
        note = Note(
            user=User.objects.get(id=request.data.get("user")),
            subject=request.data.get("body")
        )
        note.save()
        latest_note = Note.objects.latest("id")
        
        return Response({
            'status': True,
            'note_id': latest_note.id
        })

    def put(self, request, *args, **kwargs):
        note = Note(body=request.data.get("body"))
        note.id=request.data.get("note_id")
        note.save(update_fields=['body'])
        
        return Response({ 'status': True })

# get all notes for table view
class NoteListView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

# file attachments

class FileView(APIView):
    def post(self, request, *args, **kwargs):        
        serializer_class = NoteFileSerializer
        # TODO
        pass
