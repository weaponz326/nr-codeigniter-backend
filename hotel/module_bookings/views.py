from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Booking, BookedRoom
from .serializers import BookingSerializer, BookedRoomSerializer


# Create your views here.

class BookingView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        booking = Booking.objects.filter(account=account)
        serializer = BookingSerializer(booking, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class BookingDetailView(APIView):
    def get(self, request, pk, format=None):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------
# booked rooms

class BookedRoomView(APIView):
    def get(self, request, format=None):
        booking = self.request.query_params.get('booking', None)
        booked_room = BookedRoom.objects.filter(booking=booking)
        serializer = BookedRoomSerializer(booked_room, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookedRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class BookedRoomDetailView(APIView):
    def get(self, request, pk, format=None):
        booked_room = BookedRoom.objects.get(pk=pk)
        serializer = BookedRoomSerializer(booked_room)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        booked_room = BookedRoom.objects.get(pk=pk)
        serializer = BookedRoomSerializer(booked_room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        booked_room = BookedRoom.objects.get(pk=pk)
        booked_room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
