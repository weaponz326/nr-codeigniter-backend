from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Guest
from accounts.models import Profile
from .serializers import GuestSerializer


# Create your views here.

class GuestView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = GuestSerializer
        queryset = Guest.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            guest = Guest(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                guest_code=request.data.get("guest_code"),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
            )
            guest.save()
            latest_guest = Guest.objects.latest("id")

            return Response({
                'status': True,
                'guest_id': latest_guest.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class GuestListView(generics.ListAPIView):
    serializer_class = GuestSerializer

    def get_queryset(self):
        queryset = Guest.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class GuestDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
