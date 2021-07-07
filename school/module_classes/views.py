from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Class, ClassSubject
from module_students.models import Student
from .serializers import ClassSerializer, ClassListSerializer, ClassSubjectSerializer
from module_students.serializers import StudentListSerializer


# Create your views here.

class ClassView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        clas = Class.objects.filter(account=account)
        serializer = ClassListSerializer(clas, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ClassDetailView(APIView):
    def get(self, request, pk, format=None):
        clas = Class.objects.get(pk=pk)
        serializer = ClassListSerializer(clas)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        clas = Class.objects.get(pk=pk)
        serializer = ClassSerializer(clas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        clas = Class.objects.get(pk=pk)
        clas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class subjects
# -------------------------------------------------------------------------------------------------------------------

class ClassSubjectView(APIView):
    def get(self, request, format=None):
        clas = self.request.query_params.get('clas', None)
        subject = ClassSubject.objects.filter(clas=clas)
        serializer = ClassSubjectSerializer(subject, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassSubjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ClassSubjectDetailView(APIView):
    def get(self, request, pk, format=None):
        subject = ClassSubject.objects.get(pk=pk)
        serializer = ClassSubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subject = ClassSubject.objects.get(pk=pk)
        serializer = ClassSubjectSerializer(subject, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        subject = ClassSubject.objects.get(pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class students
# -------------------------------------------------------------------------------------------------------------------

class ClassStudentView(APIView):
    def get(self, request, format=None):
        clas = self.request.query_params.get('clas', None)
        student = Student.objects.filter(clas=clas)
        serializer = StudentListSerializer(student, many=True)        
        return Response(serializer.data)
