from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Contractor
from accounts.models import Profile
from .serializers import ContractorSerializer


# Create your views here.

class ContractorView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ContractorSerializer
        queryset = Contractor.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ContractorSerializer(data=request.data)
        if serializer.is_valid():
            contractor = Contractor(
                account=Profile.objects.get(id=request.data.get("production_id")),
                contractor_name=request.data.get("contractor_name"),
                category=request.data.get("category"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                country=request.data.get("country"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                website=request.data.get("website"),
                primary_contract=request.data.get("primary_contract"),
                project_name=request.data.get("project_name"),
                contract_type=request.data.get("contract_type"),
                work_description=request.data.get("work_description"),
                contract_status=request.data.get("contract_status"),
                work_start_date=request.data.get("work_start_date"),
                work_end_date=request.data.get("work_end_date"),
            )
            contractor.save()
            latest_contractor = Contractor.objects.latest("id")

            return Response({
                'status': True,
                'contractor_id': latest_contractor.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ContractorListView(generics.ListAPIView):
    serializer_class = ContractorSerializer

    def get_queryset(self):
        queryset = Contractor.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class ContractorDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
