from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Material
from accounts.models import Profile
from .serializers import MaterialSerializer


# Create your views here.

class MaterialView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = MaterialSerializer
        queryset = Material.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            material = Material(
                account=Profile.objects.get(id=request.data.get("production_id")),
                material_code=request.data.get("material_code"),
                material_name=request.data.get("material_name"),
                description=request.data.get("description"),
                category=request.data.get("category"),
                unit_price=request.data.get("unit_price"),
                quantity=request.data.get("quantity"),
            )
            material.save()
            latest_material = Material.objects.latest("id")

            return Response({
                'status': True,
                'material_id': latest_material.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class MaterialListView(generics.ListAPIView):
    serializer_class = MaterialSerializer

    def get_queryset(self):
        queryset = Material.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class MaterialDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
