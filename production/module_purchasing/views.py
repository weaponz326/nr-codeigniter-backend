from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Purchasing, PurchasingItem
from accounts.models import Profile
from .serializers import PurchasingSerializer


# Create your views here.

class PurchasingView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PurchasingSerializer
        queryset = Purchasing.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PurchasingSerializer(data=request.data)
        if serializer.is_valid():
            purchasing = Purchasing(
                account=Profile.objects.get(id=request.data.get("production_id")),
                purchasing_code=request.data.get("purchasing_code"),
                purchasing_date=request.data.get("purchasing_date"),
                supplier_name=request.data.get("supplier_name"),
                supplier_contact=request.data.get("supplier_contact"),
                supplier_invoice=request.data.get("supplier_invoice"),
            )
            purchasing.save()
            latest_purchasing = Purchasing.objects.latest("id")

            return Response({
                'status': True,
                'purchasing_id': latest_purchasing.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class PurchasingListView(generics.ListAPIView):
    serializer_class = PurchasingSerializer

    def get_queryset(self):
        queryset = Purchasing.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class PurchasingDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Purchasing.objects.all()
    serializer_class = PurchasingSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
