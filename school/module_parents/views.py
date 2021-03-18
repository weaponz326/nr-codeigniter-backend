from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Parent, ParentWard
from accounts.models import Profile
from module_students.models import Student
from .serializers import (
    ParentSerializer, 
    ParentListSerializer, 
    StudentListSerializer, 
    ParentWardSerializer, 
    ParentWardListSerializer
)


# Create your views here.

class ParentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ParentSerializer
        queryset = Parent.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            parent = Parent(
                account=Profile.objects.get(id=request.data.get("school_id")),
                parent_code=request.data.get("parent_code"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                occupation=request.data.get("occupation"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
            )
            parent.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ParentListView(generics.ListAPIView):
    serializer_class = ParentListSerializer

    def get_queryset(self):
        queryset = Parent.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class ParentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# ---------------------------------------------------------------------
# parent's wards
# all students

class StudentListView(generics.ListAPIView):
    serializer_class = StudentListSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

# wards belonging to a parent

class ParentWardView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ParentWardSerializer(data=request.data)
        if serializer.is_valid():
            ward = ParentWard(
                parent=Parent.objects.get(id=request.data.get("parent")),
                ward=Student.objects.get(id=request.data.get("ward")),
            )
            ward.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ParentWardListView(generics.ListAPIView):
    serializer_class = ParentWardListSerializer

    def get_queryset(self):
        queryset = ParentWard.objects.all()
        parent = self.request.query_params.get('parent', None)
        if parent is not None:
            queryset = queryset.filter(parent=parent)
        return queryset

class ParentWardDetailView(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ParentWard.objects.all()
    serializer_class = ParentWardSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
