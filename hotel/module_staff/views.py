from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Staff
from accounts.models import Profile
from .serializers import StaffSerializer, StaffListSerializer


# Create your views here.

class StaffView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = StaffSerializer
        queryset = Staff.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            staff = Staff(
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                date_of_birth=request.data.get("date_of_birth"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                staff_code=request.data.get("staff_code"),
                department=request.data.get("department"),
                job=request.data.get("job"),
            )
            staff.save()
            latest_staff = Staff.objects.latest("id")

            return Response({
                'status': True,
                'staff_id': latest_staff.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class StaffListView(generics.ListAPIView):
    serializer_class = StaffListSerializer

    def get_queryset(self):
        queryset = Staff.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class StaffDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
