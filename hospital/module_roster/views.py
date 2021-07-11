from django.shortcuts import render
from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Roster, 
    Shift, 
    Batch, 
    DoctorsPersonnel, 
    NursesPersonnel, 
    StaffPersonnel, 
    RosterDay, 
    RosterSheet
)
from .serializers import (
    RosterSerializer, 
    ShiftSerializer, 
    BatchSerializer,    
    RosterDaySerializer,
    RosterSheetSerializer,
    DoctorsPersonnelSerializer,
    DoctorsPersonnelListSerializer,
    NursesPersonnelSerializer,
    NursesPersonnelListSerializer,
    StaffPersonnelSerializer,
    StaffPersonnelListSerializer,
)
from module_doctors.models import Doctor
from module_nurses.models import Nurse
from module_staff.models import Staff


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
        shift = Shift.objects.get(pk=pk)
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

class RefreshPersonnelView(APIView):
    def get(self, request, format=None):        
        roster = self.request.query_params.get('roster', None)
        roster_instance = Roster.objects.get(id=roster)
        account = roster_instance.account
        
        if roster_instance.source == "Doctors":
            doctor_set = Doctor.objects.filter(account=account)
            for doctor in doctor_set:
                if not DoctorsPersonnel.objects.filter(roster=roster):
                    personnel = DoctorsPersonnel(roster=roster_instance, doctor=doctor)
                    personnel.save()
        elif roster_instance.source == "Nurses":
            nurse_set = Nurse.objects.filter(account=account)
            for nurse in nurse_set:
                if not NursesPersonnel.objects.filter(roster=roster):
                    personnel = NursesPersonnel(roster=roster_instance, nurse=nurse)
                    personnel.save()
        elif roster_instance.source == "Staff":
            staff_set = Staff.objects.filter(account=account)
            for staff in staff_set:
                if not StaffPersonnel.objects.filter(roster=roster):
                    personnel = StaffPersonnel(roster=roster_instance, staff=staff)
                    personnel.save()

        return Response({ 'message' : 'OK' })

class PersonnelView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        roster_instance = Roster.objects.get(id=roster)

        if roster_instance.source == "Doctors":
            personnel = DoctorsPersonnel.objects.filter(roster=roster)
            serializer = DoctorsPersonnelListSerializer(personnel, many=True)        
            return Response(serializer.data)
        elif roster_instance.source == "Nurses":
            personnel = NursesPersonnel.objects.filter(roster=roster)
            serializer = NursesPersonnelListSerializer(personnel, many=True)        
            return Response(serializer.data)
        elif roster_instance.source == "Staff":
            personnel = StaffPersonnel.objects.filter(roster=roster)
            serializer = StaffPersonnelListSerializer(personnel, many=True)        
            return Response(serializer.data)

class PersonnelDetailView(APIView):
    def put(self, request, pk, format=None):
        batch = Batch.objects.get(pk=pk)
        roster = Roster.objects.get(id=batch.roster)

        if roster.source == "Doctors":
            serializer = DoctorsPersonnelSerializer(batch, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({ 'message': 'OK', 'data': serializer.data })
            return Response(serializer.errors)
        elif roster.source == "Nurses":
            serializer = NursesPersonnelSerializer(batch, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({ 'message': 'OK', 'data': serializer.data })
            return Response(serializer.errors)
        elif roster.source == "Staff":
            serializer = StaffPersonnelSerializer(batch, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({ 'message': 'OK', 'data': serializer.data })
            return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        roster = Batch.objects.get(pk=pk)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------
# roster sheet

class RefreshSheetView(APIView):
    def get(self, request, format=None):
        
        def daterange(from_date, to_date):
            for n in range(int((to_date - from_date).days)):
                yield from_date + timedelta(n)

        roster = self.request.query_params.get('roster', None)
        roster_instance = Roster.objects.get(id=roster)
        
    	# fill days table        
        from_date = roster_instance.from_date
        to_date = roster_instance.to_date

        add_list = []
        delete_list = []
        day_set = RosterDay.objects.filter(roster=roster)

        if day_set.exists():
            for new_day in daterange(from_date, to_date):
                for day in day_set.iterator():
                    if (new_day != day) and (new_day > to_date):
                        add_list.append(RosterDay(roster=roster_instance, day=str(new_day)))
                    if (new_day != day) and (new_day < from_date):
                        delete_list.append({roster:roster_instance, day:day})

            if not add_list == []: RosterDay.objects.bulk_create(add_list)
            if not delete_list == []: RosterDay.objects.filter(roster__in=delete_list[roster], day__in=delete_list[day])
        else:
            for new_day in daterange(from_date, to_date):
                add_list.append(RosterDay(roster=roster_instance, day=str(new_day)))
            if not add_list == []: RosterDay.objects.bulk_create(add_list)

        return Response({ 'message' : 'OK' })

class RosterDayView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        day = RosterDay.objects.filter(roster=roster)
        serializer = RosterDaySerializer(day, many=True)        
        return Response(serializer.data)

# TODO: insert and get sheet batches
class RosterSheetView(APIView):
    def get(self, request, format=None):
        return Response({ 'message' : 'TODO' })

    def post(self, request, format=None):
        return Response({ 'message' : 'TODO' })
