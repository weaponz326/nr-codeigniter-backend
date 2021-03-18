from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import filters

from .models import Rink
from accounts.models import Profile
# from module_students.models import Student
# from module_teachers.models import Teacher
# from module_subjects.models import Subject
from .serializers import RinkSerializer, ProfileSerializer, RinkDetailSerializer
# from module_students.serializers import StudentSerializer
# from module_teachers.serializers import TeacherSerializer
# from module_subjects.serializers import SubjectSerializer


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
    search_fields = ['name']
    
class SearchDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# rink type sources

# class StudentListView(generics.ListAPIView):
#     serializer_class = StudentSerializer

#     def get_queryset(self):
#         queryset = Student.objects.all()
#         school = self.request.query_params.get('school', None)
#         if school is not None:
#             queryset = queryset.filter(account=school)
#         return queryset

# class TeacherListView(generics.ListAPIView):
#     serializer_class = TeacherSerializer

#     def get_queryset(self):
#         queryset = Teacher.objects.all()
#         school = self.request.query_params.get('school', None)
#         if school is not None:
#             queryset = queryset.filter(account=school)
#         return queryset

# class SubjectListView(generics.ListAPIView):
#     serializer_class = SubjectSerializer

#     def get_queryset(self):
#         queryset = Subject.objects.all()
#         school = self.request.query_params.get('school', None)
#         if school is not None:
#             queryset = queryset.filter(account=school)
#         return queryset

# list all rinks of a user
class RinkListView(generics.ListAPIView):
    serializer_class = RinkDetailSerializer

    def get_queryset(self):
        queryset = Rink.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            # queryset = queryset.filter(recipient__id=user).filter(sender__id=user)
            queryset = queryset.filter(recipient__id=user)
        return queryset

# get a specific rink
class RinkDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Rink.objects.all()
    serializer_class = RinkDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

# get single dource for rink details

# class StudentDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class TeacherDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class SubjectDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
