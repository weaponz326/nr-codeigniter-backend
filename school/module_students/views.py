from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Student
from accounts.models import Profile
from module_classes.models import Class
from .serializers import StudentSerializer, StudentListSerializer


# Create your views here.

class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = StudentSerializer
        queryset = Student.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = Student(
                account=Profile.objects.get(id=request.data.get("school_id")),
                clas=Class.objects.get(id=request.data.get("clas")),
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
                student_code=request.data.get("student_code"),
                admission_date=request.data.get("admission_date"),
                previous_school=request.data.get("previous_school"),
            )
            student.save()
            latest_student = Student.objects.latest("id")

            return Response({
                'status': True,
                'student_id': latest_student.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class StudentListView(generics.ListAPIView):
    serializer_class = StudentListSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class StudentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
