from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Reservation
from .serializers import ReservationSerializer


# Create your views here.

class ReservationView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        reservation = Reservation.objects.filter(account=account)
        serializer = ReservationSerializer(reservation, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ReservationDetailView(APIView):
    def get(self, request, pk, format=None):
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reservation = Reservation.objects.get(pk=pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
