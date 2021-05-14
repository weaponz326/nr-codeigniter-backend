from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Timetable
from .serializers import TimetableSerializer


# Create your views here.

class TimetableView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        timetable = Timetable.objects.filter(account=account)
        serializer = TimetableSerializer(timetable, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TimetableSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TimetableDetailView(APIView):
    def get(self, request, pk, format=None):
        timetable = Timetable.objects.get(pk=pk)
        serializer = TimetableSerializer(timetable)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        timetable = Timetable.objects.get(pk=pk)
        serializer = TimetableSerializer(timetable, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        timetable = Timetable.objects.get(pk=pk)
        timetable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
