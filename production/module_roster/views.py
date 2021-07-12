from django.shortcuts import render
from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Roster, 
    Shift, 
    Batch, 
    WorkerPersonnel, 
    RosterDay, 
    RosterSheet
)
from .serializers import (
    RosterSerializer, 
    ShiftSerializer, 
    BatchSerializer,
    WorkerPersonnelSerializer,
    WorkerPersonnelListSerializer,
    RosterDaySerializer,
    RosterSheetSerializer
)
from module_workers.models import Worker


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
        worker_set = Worker.objects.filter(account=account)

        for worker in worker_set:
            if not WorkerPersonnel.objects.filter(roster=roster):
                personnel = WorkerPersonnel(roster=roster_instance, worker=worker)
                personnel.save()

        return Response({ 'message' : 'OK' })

class WorkerPersonnelView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        personnel = WorkerPersonnel.objects.filter(roster=roster)
        serializer = WorkerPersonnelListSerializer(personnel, many=True)        
        return Response(serializer.data)

class WorkerPersonnelDetailView(APIView):
    def put(self, request, pk, format=None):
        personnel = Batch.objects.get(pk=pk)
        serializer = WorkerPersonnelSerializer(personnel, data=request.data)
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

        # TODO: innitiate sheet fields

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
