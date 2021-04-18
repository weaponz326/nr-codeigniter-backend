from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Manufacturing
from accounts.models import Profile
from module_products.models import Product
from .serializers import ManufacturingSerializer


# Create your views here.

class ManufacturingView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ManufacturingSerializer
        queryset = Manufacturing.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ManufacturingSerializer(data=request.data)
        if serializer.is_valid():
            manufacturing = Manufacturing(
                account=Profile.objects.get(id=request.data.get("production_id")),
                product=Product.objects.get(id=request.data.get("produc_id")),
                manufacturing_code=request.data.get("manufacturing_code"),
                description=request.data.get("description"),
                start_date=request.data.get("start_date"),
                end_date=request.data.get("end_date"),
                quantity=request.data.get("quantity"),
                manufacturing_status=request.data.get("manufacturing_status"),
                remarks=request.data.get("remarks"),
            )
            manufacturing.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ManufacturingListView(generics.ListAPIView):
    serializer_class = ManufacturingSerializer

    def get_queryset(self):
        queryset = Manufacturing.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class ManufacturingDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Manufacturing.objects.all()
    serializer_class = ManufacturingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
