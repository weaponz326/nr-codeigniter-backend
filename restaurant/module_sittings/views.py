from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Sitting
from accounts.models import Profile
from .serializers import SittingSerializer


# Create your views here.

class SittingView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SittingSerializer
        queryset = Sitting.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = SittingSerializer(data=request.data)
        if serializer.is_valid():
            sitting = Sitting(
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                sitting_code=request.data.get("sitting_code"),
                sitting_date=request.data.get("sitting_date"),
                arrival_time=request.data.get("arrival_time"),
                departure_time=request.data.get("departure_time"),
                customer_name=request.data.get("customer_name"),
                number_guests=request.data.get("number_guests"),
            )
            sitting.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class SittingListView(generics.ListAPIView):
    serializer_class = SittingSerializer

    def get_queryset(self):
        queryset = Sitting.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class SittingDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Sitting.objects.all()
    serializer_class = SittingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
