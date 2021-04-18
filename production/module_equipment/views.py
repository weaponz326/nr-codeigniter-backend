from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Equipment
from accounts.models import Profile
from .serializers import EquipmentSerializer


# Create your views here.

class EquipmentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = EquipmentSerializer
        queryset = Equipment.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            equipment = Equipment(
                account=Profile.objects.get(id=request.data.get("production_id")),
                equipment_code=request.data.get("equipment_code"),
                equipment_name=request.data.get("equipment_name"),
                equipment_type=request.data.get("equipment_type"),
                category=request.data.get("category"),
                brand=request.data.get("brand"),
                model=request.data.get("model"),
                serial_number=request.data.get("serial_number"),
                description=request.data.get("description"),
                location=request.data.get("location"),
                condition=request.data.get("condition"),
                equipment_status=request.data.get("equipment_status"),
            )
            equipment.save()
            latest_equipment = Equipment.objects.latest("id")

            return Response({
                'status': True,
                'equipment_id': latest_equipment.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class EquipmentListView(generics.ListAPIView):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class EquipmentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
