from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Timetable, TimetablePeriod, TimetableClass, TimetableSheet
from .serializers import TimetableSerializer, TimetablePeriodSerializer, TimetableClassSerializer, TimetableSheetSerializer


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

# --------------------------------------------------------------------------------------------------------------
# timetable config

class TimetablePeriodView(APIView):
    def get(self, request, format=None):
        timetable = self.request.query_params.get('timetable', None)
        period = TimetablePeriod.objects.filter(timetable=timetable)
        serializer = TimetablePeriodSerializer(period, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TimetablePeriodSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TimetableClassView(APIView):
    def get(self, request, format=None):
        timetable = self.request.query_params.get('timetable', None)
        clas = TimetableClass.objects.filter(timetable=timetable)
        serializer = TimetableClassSerializer(clas, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TimetableClassSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TimetableClassDetailView(APIView):
    def get(self, request, pk, format=None):
        timetable_class = TimetableClass.objects.get(pk=pk)
        serializer = TimetableClassSerializer(timetable_class)
        return Response(serializer.data)

# -----------------------------------------------------------------------------------------------------------------------
# timetable sheet

class RefreshSheetView(APIView):
    def get(self, request, format=None):
        timetable = self.request.query_params.get('timetable', None)
        timetable_instance = Timetable.objects.get(id=timetable)
        class_set = TimetableClass.objects.filter(timetable=timetable)
        period_set = TimetablePeriod.objects.filter(timetable=timetable)
        sheet_set = TimetableSheet.objects.filter(timetable=timetable)

        sheet_list = []

        if class_set.exists():
            for clas in class_set.iterator():
                if period_set.exists():
                    for period in period_set.iterator():
                        
                        this_sheet = TimetableSheet.objects.filter(timetable_class=clas.id, timetable_period=period.id)
                        if not this_sheet.exists():
                            sheet_list.append(TimetableSheet(timetable=timetable_instance, timetable_class=clas, timetable_period=period, subjects={}))

        if not sheet_list == []: TimetableSheet.objects.bulk_create(sheet_list)
        return Response({ 'message' : 'OK' })

class FullSheetView(APIView):
    def get(self, request, format=None):
        timetable = self.request.query_params.get('timetable', None)
        sheet = TimetableSheet.objects.filter(timetable=timetable)
        serializer = TimetableSheetSerializer(sheet, many=True)        
        return Response(serializer.data)

class ClassSheetView(APIView):
    def get(self, request, format=None):
        timetable_class = self.request.query_params.get('timetable_class', None)
        sheet = TimetableSheet.objects.filter(timetable_class=timetable_class)
        serializer = TimetableSheetSerializer(sheet, many=True)        
        return Response(serializer.data)
