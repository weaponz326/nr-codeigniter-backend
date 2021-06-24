from django.shortcuts import render
from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Roster, Shift, Batch, DoctorsPersonnel, RosterDays, RosterSheet
from .serializers import RosterSerializer, ShiftSerializer, BatchSerializer
from module_doctors.models import Doctor


# Create your views here.

class RosterView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        roster = Roster.objects.filter(account=account)
        serializer = RosterSerializer(roster, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class RosterDetailView(APIView):
    def get(self, request, pk, format=None):
        roster = Roster.objects.get(pk=pk)
        serializer = RosterSerializer(roster)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        roster = Roster.objects.get(pk=pk)
        serializer = RosterSerializer(roster, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        roster = Roster.objects.get(pk=pk)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------------
# shifts

class ShiftView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        shift = Shift.objects.filter(roster=roster)
        serializer = ShiftSerializer(shift, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ShiftDetailView(APIView):
    def get(self, request, pk, format=None):
        shift = Shift.objects.get(pk=pk)
        serializer = ShiftSerializer(shift)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        shift = Batch.objects.get(pk=pk)
        serializer = ShiftSerializer(shift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        roster = Roster.objects.get(pk=pk)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------------------
# batches

class BatchView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        batch = Batch.objects.filter(roster=roster)
        serializer = BatchSerializer(batch, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class BatchDetailView(APIView):
    def get(self, request, pk, format=None):
        batch = Batch.objects.get(pk=pk)
        serializer = BatchSerializer(batch)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        batch = Batch.objects.get(pk=pk)
        serializer = BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        roster = Batch.objects.get(pk=pk)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------
# personnel

# TODO: have to do it for all possible sources
class RefreshPersonnelView(APIView):
    def get(self, request, format=None):        
        roster = self.request.query_params.get('roster', None)
        account = roster.account
        doctor_set = Doctor.objects.filter(account=account)

        for doctor in doctor_set:
            if not DoctorsPersonnel.objects.get(roster=roster):
                personnel = DoctorsPersonnel(roster=roster.id, doctor=doctor.id)
                personnel.save()

        return Response({ 'message' : 'OK' })

# -----------------------------------------------------------------------------------------------------------
# roster sheet

class RefreshSheetView(APIView):
    def get(self, request, format=None):
        
        def daterange(from_date, to_date):
            for n in range(int((to_date - from_date).days)):
                yield from_date + timedelta(n)

        # to be used in filling both days and sheet tables
        roster = self.request.query_params.get('roster', None)
        
        from_date = roster.from_date
        to_date = roster.to_date
        days = {};

        for day in daterange(from_date, to_date):
            days.update(day)

        roster_days = RosterDays(days=days)
        roster_days.roster = roster
        roster_days.save()    

        return Response({ 'message' : 'OK' })
