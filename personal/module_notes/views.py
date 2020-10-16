from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.parsers import FileUploadParser

from .models import Note, NoteFile
from .serializers import NoteSerializer, NoteFileSerializer

# Create your views here.

class NoteView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = NoteSerializer
        queryset = Note.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = Note(data=request.data)
        if serializer.is_valid():
            note = Note(
                user=User(id=request.data.get("user")),
                subject=request.data.get("subject"),
                body=request.data.get("body")
            )
            note.save()
            latest_note = Note.objects.latest("id")
            
            return Response({
                'status': True,
                'note_id': latest_note.id
            })
        else:
            return Response({'status': False})

# update and delete note
class NoteDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# get all notes for table view
class NoteListView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

# update and get subject and body individually

class SubjectView(APIView):  
    def get(self, request, *args, **kwargs):
        serializer_class = NoteSerializer
        queryset = Note.objects.all()
        note = queryset.get(id=request.query_params.get('note_id', None))

        return Response({ 'subject': note.subject })

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

    def put(self, request, *args, **kwargs):
        note = Note(body=request.data.get("body"))
        note.id=request.data.get("note_id")
        note.save(update_fields=['body'])
        
        return Response({ 'status': True })

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