from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Room
from accounts.models import Profile
from .serializers import RoomSerializer


# Create your views here.

class RoomView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = RoomSerializer
        queryset = Room.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = Room(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                room_number=request.data.get("room_number"),
                room_type=request.data.get("room_type"),
                location=request.data.get("location"),
                rate=request.data.get("rate"),
                features=request.data.get("features"),
                room_status=request.data.get("room_status"),
            )
            room.save()
            latest_room = Room.objects.latest("id")

            return Response({
                'status': True,
                'room_id': latest_room.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class RoomDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
