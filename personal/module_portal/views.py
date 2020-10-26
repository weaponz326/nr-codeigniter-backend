from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import filters

from .models import Rink
from users.models import Profile
from module_tasks.models import Task
from module_calendar.models import Appointment
from module_notes.models import Note
from .serializers import RinkSerializer, ProfileSerializer, RinkDetailSerializer
from module_tasks.serializers import TaskSerializer
from module_calendar.serializers import AppointmentSerializer
from module_notes.serializers import NoteSerializer


# Create your views here.


class RinkView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = RinkSerializer
        queryset = Rink.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = RinkSerializer(data=request.data)
        if serializer.is_valid():
            rink = Rink(
                sender=Profile.objects.get(id=request.data.get("sender")),
                recipient=Profile.objects.get(id=request.data.get("recipient")),
                rink_type=request.data.get("rink_type"),
                rink_source=request.data.get("rink_source"),
                comment=request.data.get("comment")
            )
            rink.save()
            latest_rink = Rink.objects.latest("id")

            return Response({ 
                'status': True ,
                'rink_id': latest_rink.id
            })
        else:
            return Response({ 'status': False })

class SearchListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name']
    
class SearchDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# rink type sources

class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class NoteListView(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

# list all rinks of a user
class RinkListView(generics.ListAPIView):
    serializer_class = RinkDetailSerializer

    def get_queryset(self):
        queryset = Rink.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(sender__id=user)
        return queryset

# get a specific rink
class RinkDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Rink.objects.all()
    serializer_class = RinkDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# get single dource for rink details

class TaskDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class AppointmentDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class NoteDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)