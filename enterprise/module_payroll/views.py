from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from accounts.models import Profile
from .models import Payroll
from .serializers import PayrollSerializer


# Create your views here.

class PayrollView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = PayrollSerializer
        queryset = Payroll.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = PayrollSerializer(data=request.data)
        if serializer.is_valid():
            payroll = Payroll(
                payroll=Profile.objects.get(id=request.data.get("enterprise_id")),
                payroll_name=request.data.get("payroll_name"),
                payroll_status=request.data.get("payroll_status"),
                date_generated=request.data.get("date_generated"),
                month=request.data.get("month"),
                year=request.data.get("year"),
            )
            payroll.save()
            latest_payroll = Payroll.objects.latest("id")

            return Response({
                'status': True,
                'payroll_id': latest_payroll.id
            })
        else:
            return Response({ 'status': False })

class PayrollListView(generics.ListAPIView):
    serializer_class = PayrollSerializer

    def get_queryset(self):
        queryset = Payroll.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class PayrollDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
