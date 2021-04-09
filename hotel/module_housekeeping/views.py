from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Housekeeping
from accounts.models import Profile
from module_rooms.models import Room
from .serializers import HousekeepingSerializer


# Create your views here.

class HousekeepingView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = HousekeepingSerializer
        queryset = Housekeeping.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = HousekeepingSerializer(data=request.data)
        if serializer.is_valid():
            housekeeping = Housekeeping(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                room=Room.objects.get(id=request.data.get("room_id")),
                housekeeping_code=request.data.get("housekeeping_code"),
                housekeeping_date=request.data.get("housekeeping_date"),
            )
            housekeeping.save()
            latest_housekeeping = Housekeeping.objects.latest("id")

            return Response({
                'status': True,
                'housekeeping_id': latest_housekeeping.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class HousekeepingListView(generics.ListAPIView):
    serializer_class = HousekeepingSerializer

    def get_queryset(self):
        queryset = Housekeeping.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class HousekeepingDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Housekeeping.objects.all()
    serializer_class = HousekeepingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
