from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Nurse
from accounts.models import Profile
from .serializers import NurseSerializer, NurseListSerializer


# Create your views here.

class NurseView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = NurseSerializer
        queryset = Nurse.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            nurse = Nurse(
                account=Profile.objects.get(id=request.data.get("hospital_id")),
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
                nurse_code=request.data.get("nurse_code"),
                department=request.data.get("department"),
                work_status=request.data.get("work_status"),
                started_work=request.data.get("started_work"),
                ended_work=request.data.get("ended_work"),
            )
            nurse.save()
            latest_nurse = Nurse.objects.latest("id")

            return Response({
                'status': True,
                'nurse_id': latest_nurse.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class NurseListView(generics.ListAPIView):
    serializer_class = NurseListSerializer

    def get_queryset(self):
        queryset = Nurse.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(account=hospital)
        return queryset

class NurseDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
