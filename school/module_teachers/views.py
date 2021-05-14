from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Teacher
from accounts.models import Profile
from .serializers import TeacherSerializer, TeacherListSerializer


# Create your views here.

class TeacherView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        teacher = Teacher.objects.filter(account=account)
        serializer = TeacherListSerializer(teacher, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TeacherDetailView(APIView):
    def get(self, request, pk, format=None):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = Teacher.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serialzer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
