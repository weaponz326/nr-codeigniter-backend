from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Payroll, PayrollSheet
from module_employees.models import Employee
from .serializers import PayrollSerializer, PayrollSheetSerializer, PayrollSheetListSerializer


# Create your views here.

class PayrollView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payroll = Payroll.objects.filter(account=account)
        serializer = PayrollSerializer(payroll, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PayrollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PayrollDetailView(APIView):
    def get(self, request, pk, format=None):
        payroll = Payroll.objects.get(pk=pk)
        serializer = PayrollSerializer(payroll)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payroll = Payroll.objects.get(pk=pk)
        serializer = PayrollSerializer(payroll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        payroll = Payroll.objects.get(pk=pk)
        payroll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------
# payroll sheet

class PayrollSheetView(APIView):
    def get(self, request, format=None):
        payroll = self.request.query_params.get('payroll', None)
        sheet = PayrollSheet.objects.filter(payroll=payroll)
        serializer = PayrollSheetListSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PayrollSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PayrollSheetDetailView(APIView):
    def get(self, request, pk, format=None):
        sheet = PayrollSheet.objects.get(pk=pk)
        serializer = PayrollSheetListSerializer(sheet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        sheet = PayrollSheet.objects.get(pk=pk)
        serializer = PayrollSheetSerializer(sheet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        sheet = PayrollSheet.objects.get(pk=pk)
        sheet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------

class RefreshSheetView(APIView):
    def get(self, request, format=None):
        payroll = self.request.query_params.get('payroll', None)
        payroll_instance = Payroll.objects.get(id=payroll)
        account = payroll_instance.account.id
        employee_set = Employee.objects.filter(account=account)

        employee_list = []

        if employee_set.exists():
            for employee in employee_set.iterator():
                this_employee = PayrollSheet.objects.filter(employee=employee.id)
                if not this_employee.exists():
                    employee_list.append(PayrollSheet(payroll=payroll_instance, employee=employee))
            if not employee_list == []: PayrollSheet.objects.bulk_create(employee_list)

        return Response({ 'message' : 'OK' })
