from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Section, SectionStudent
from .serializers import SectionSerializer, SectionListSerializer, SectionStudentSerializer, SectionStudentListSerializer


# Create your views here.

class SectionView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        section = Section.objects.filter(account=account)
        serializer = SectionListSerializer(section, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SectionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SectionDetailView(APIView):
    def get(self, request, pk, format=None):
        section = Section.objects.get(pk=pk)
        serializer = SectionListSerializer(section)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        section = Section.objects.get(pk=pk)
        serializer = SectionSerializer(section, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        section = Section.objects.get(pk=pk)
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------
# section students

class SectionStudentView(APIView):
    def get(self, request, format=None):
        section = self.request.query_params.get('section', None)
        section_student = SectionStudent.objects.filter(section=section)
        serializer = SectionStudentListSerializer(section_student, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SectionStudentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class SectionStudentDetailView(APIView):
    def get(self, request, pk, format=None):
        section_student = SectionStudent.objects.get(pk=pk)
        serializer = SectionStudentListSerializer(section_student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        section_student = Section.objects.get(pk=pk)
        serializer = SectionStudentSerializer(section_student, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        section_student = SectionStudent.objects.get(pk=pk)
        section_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
