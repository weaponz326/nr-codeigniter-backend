from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Drug
from accounts.models import Profile
from .serializers import DrugSerializer


# Create your views here.

class DrugView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = DrugSerializer
        queryset = Drug.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = DrugSerializer(data=request.data)
        if serializer.is_valid():
            drug = Drug(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
                ndc_number=request.data.get("ndc_number"),
                drug_name=request.data.get("drug_name"),
                generic_name=request.data.get("generic_name"),
                category=request.data.get("category"),
                manufacturer=request.data.get("manufacturer"),
                drug_type=request.data.get("drug_type"),
                unit_dose=request.data.get("unit_dose"),
                unit_price=request.data.get("unit_price"),
                batch_number=request.data.get("batch_number"),
                purchased_date=request.data.get("purchased_date"),
                initial_quantity=request.data.get("initial_quantity"),
                dispensed_quantity=request.data.get("dispensed_quantity"),
                remaining_quantity=request.data.get("remaining_quantity"),
                manufacturing_date=request.data.get("manufacturing_date"),
                expiry_date=request.data.get("expiry_date"),
                storage_location=request.data.get("storage_location"),
                storage_bin=request.data.get("storage_bin"),
                refill_ordered=request.data.get("refill_ordered"),
            )
            drug.save()
            latest_drug = Drug.objects.latest("id")

            return Response({
                'status': True,
                'drug_id': latest_drug.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class DrugListView(generics.ListAPIView):
    serializer_class = DrugSerializer

    def get_queryset(self):
        queryset = Drug.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class DrugDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
