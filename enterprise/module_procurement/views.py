from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Procurement
from accounts.models import Profile
from .serializers import ProcurementSerializer


# Create your views here.

class ProcurementView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ProcurementSerializer
        queryset = Procurement.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ProcurementSerializer(data=request.data)
        if serializer.is_valid():
            procurement = Procurement(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                order_code=request.data.get("order_code"),
                order_date=request.data.get("order_date"),
                order_type=request.data.get("order_type"),
                description=request.data.get("description"),
                project=request.data.get("project"),
                recepient=request.data.get("recepient"),
                vendor=request.data.get("vendor"),
                vendor_phone=request.data.get("vendor_phone"),
                vendor_email=request.data.get("vendor_email"),
                vendor_address=request.data.get("vendor_address"),
                order_status=request.data.get("order_status"),
            )
            procurement.save()
            latest_procurement = Procurement.objects.latest("id")

            return Response({
                'status': True,
                'procurement_id': latest_procurement.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ProcurementListView(generics.ListAPIView):
    serializer_class = ProcurementSerializer

    def get_queryset(self):
        queryset = Procurement.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class ProcurementDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Procurement.objects.all()
    serializer_class = ProcurementSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
