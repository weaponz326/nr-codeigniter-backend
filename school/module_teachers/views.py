from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Teacher
from accounts.models import Profile
from .serializers import TeacherSerializer, TeacherListSerializer


# Create your views here.

class TeacherView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = TeacherSerializer
        queryset = Teacher.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            teacher = Teacher(
                account=Profile.objects.get(id=request.data.get("school_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                date_of_birth=request.data.get("dob"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                teacher_code=request.data.get("teacher_code"),
                department=request.data.get("department"),
                grade=request.data.get("grade"),
                education=request.data.get("education"),
            )
            teacher.save()
            latest_teacher = Teacher.objects.latest("id")

            return Response({
                'status': True,
                'teacher': latest_teacher.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class TeacherListView(generics.ListAPIView):
    serializer_class = TeacherListSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class TeacherDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
