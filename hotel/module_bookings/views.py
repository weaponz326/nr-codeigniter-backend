from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Booking
from accounts.models import Profile
from .serializers import BookingSerializer


# Create your views here.

class BookingView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = BookingSerializer
        queryset = Booking.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = Booking(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                booking_code=request.data.get("booking_code"),
                booking_date=request.data.get("booking_date"),
                guest_name=request.data.get("guest_name"),
                expected_arrival=request.data.get("expected_arrival"),
                booking_status=request.data.get("booking_status"),
            )
            booking.save()
            latest_booking = Booking.objects.latest("id")

            return Response({
                'status': True,
                'booking_id': latest_booking.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class BookingDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
