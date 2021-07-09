from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Appraisal, AppraisalForm
from module_employees.models import Employee
from .serializers import AppraisalSerializer, AppraisalFormSerializer, AppraisalFormListSerializer


# Create your views here.

class AppraisalView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        appraisal = Appraisal.objects.filter(account=account)
        serializer = AppraisalSerializer(appraisal, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppraisalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AppraisalDetailView(APIView):
    def get(self, request, pk, format=None):
        appraisal = Appraisal.objects.get(pk=pk)
        serializer = AppraisalSerializer(appraisal)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        appraisal = Appraisal.objects.get(pk=pk)
        serializer = AppraisalSerializer(appraisal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        appraisal = Appraisal.objects.get(pk=pk)
        appraisal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------------
# appraisal form

class AppraisalFormView(APIView):
    def get(self, request, format=None):
        appraisal = self.request.query_params.get('appraisal', None)
        form = AppraisalForm.objects.filter(appraisal=appraisal)
        serializer = AppraisalFormListSerializer(form, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AppraisalFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AppraisalFormDetailView(APIView):
    def get(self, request, pk, format=None):
        form = AppraisalForm.objects.get(pk=pk)
        serializer = AppraisalFormListSerializer(form)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        form = AppraisalForm.objects.get(pk=pk)
        serializer = AppraisalFormListSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        form = AppraisalForm.objects.get(pk=pk)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------------------------

class RefreshAppraisalView(APIView):
    def get(self, request, format=None):
        appraisal = self.request.query_params.get('appraisal', None)
        appraisal_instance = Appraisal.objects.get(id=appraisal)
            
        employee_set = Employee.objects.filter(account=appraisal_instance.account)
        employee_list = []

        if employee_set.exists():
            for employee in employee_set.iterator():
                if not AppraisalForm.objects.filter(appraisal=appraisal, employee=employee.id).exists():
                    employee_list.append(AppraisalForm(appraisal=appraisal_instance, employee=employee))
            if not employee_list == []: AppraisalForm.objects.bulk_create(employee_list)

        return Response({ 'message' : 'OK' })

