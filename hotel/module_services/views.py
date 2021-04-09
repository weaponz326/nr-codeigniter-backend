from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Service
from accounts.models import Profile
from .serializers import ServiceSerializer


# Create your views here.

class ServiceView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ServiceSerializer
        queryset = Service.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            service = Service(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                service_code=request.data.get("service_code"),
                service_type=request.data.get("service_type"),
                service_date=request.data.get("service_date"),
            )
            service.save()
            latest_service = Service.objects.latest("id")

            return Response({
                'status': True,
                'service_id': latest_service.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class ServiceDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
