from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Employee
from accounts.models import Profile
from .serializers import EmployeeSerializer, EmployeeListSerializer


# Create your views here.

class EmployeeView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = EmployeeSerializer
        queryset = Employee.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = Employee(
                account=Profile.objects.get(id=request.data.get("enterprise_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                date_of_birth=request.data.get("date_of_birth"),
                photo=request.data.get("photo"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                employee_code=request.data.get("employee_code"),
                department=request.data.get("department"),
                work_status=request.data.get("work_status"),
                started_work=request.data.get("started_work"),
                ended_work=request.data.get("ended_work"),
            )
            employee.save()
            latest_employee = Employee.objects.latest("id")

            return Response({
                'status': True,
                'employee_id': latest_employee.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class EmployeeDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
