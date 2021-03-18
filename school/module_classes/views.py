from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Class, ClassSubject
from accounts.models import Profile
from module_subjects.models import Subject
from .serializers import ClassSerializer, SubjectSerializer, ClassSubjectSerializer, ClassSubjectListSerializer


# Create your views here.

class ClassView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ClassSerializer
        queryset = Class.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            clas = Class(
                account=Profile.objects.get(id=request.data.get("school_id")),
                class_name=request.data.get("class_name"),
                department=request.data.get("department"),
                location=request.data.get("location"),
            )
            clas.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ClassListView(generics.ListAPIView):
    serializer_class = ClassSerializer

    def get_queryset(self):
        queryset = Class.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class ClassDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class' subjects

class ClassSubjectListView(generics.ListAPIView):
    serializer_class = ClassSubjectListSerializer

    def get_queryset(self):
        queryset = ClassSubject.objects.all()
        clas = self.request.query_params.get('clas', None)
        if clas is not None:
            queryset = queryset.filter(clas=clas)
        return queryset

class AllSubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset
