from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Checkin
from accounts.models import Profile
from .serializers import CheckinSerializer


# Create your views here.

class CheckinView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CheckinSerializer
        queryset = Checkin.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = CheckinSerializer(data=request.data)
        if serializer.is_valid():
            checkin = Checkin(
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                checkin_code=request.data.get("checkin_code"),
                checkin_date=request.data.get("checkin_date"),
                checkout_date=request.data.get("checkout_date"),
                number_nights=request.data.get("number_nights"),
            )
            checkin.save()
            latest_checkin = Checkin.objects.latest("id")

            return Response({
                'status': True,
                'checkin_id': latest_checkin.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class CheckinListView(generics.ListAPIView):
    serializer_class = CheckinSerializer

    def get_queryset(self):
        queryset = Checkin.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class CheckinDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Checkin.objects.all()
    serializer_class = CheckinSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
