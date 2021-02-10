from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Reservation
from accounts.models import Profile
from .serializers import ReservationSerializer


# Create your views here.

class ReservationView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ReservationSerializer
        queryset = Reservation.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = Reservation(
                restaurant=Profile.objects.get(id=request.data.get("restaurant_id")),
                reservation_code=request.data.get("reservation_code"),
                reservation_date=request.data.get("reservation_date"),
                customer_name=request.data.get("customer_name"),
                number_guests=request.data.get("number_guests"),
                number_tables=request.data.get("number_tables"),
                arrival_date=request.data.get("arrival_date"),
                reservation_status=request.data.get("reservation_status"),
            )
            reservation.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset

class ReservationDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
