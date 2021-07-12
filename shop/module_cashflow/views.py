from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Cashflow,
    DailyInflow,
    DailyOutflow,
    WeeklyInflow,
    WeeklyOutflow,
    MonthlyInflow,
    MonthlyOutflow,
    QuarterlyInflow,
    QuarterlyOutflow
)
from .serializers import (
    CashflowSerializer,
    DailyInflowSerializer,
    DailyOutflowSerializer,
    WeeklyInflowSerializer,
    WeeklyOutflowSerializer,
    MonthlyInflowSerializer,
    MonthlyOutflowSerializer,
    QuarterlyInflowSerializer,
    QuarterlyOutflowSerializer
)


# Create your views here.

class CashflowView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        cashflow = Cashflow.objects.filter(account=account)
        serializer = CashflowSerializer(cashflow, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CashflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class CashflowDetailView(APIView):
    def get(self, request, pk, format=None):
        cashflow = Cashflow.objects.get(pk=pk)
        serializer = CashflowSerializer(cashflow)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cashflow = Cashflow.objects.get(pk=pk)
        serializer = CashflowSerializer(cashflow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        cashflow = Cashflow.objects.get(pk=pk)
        cashflow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# sheets

# daily sheets

class DailyInflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = Cashflow.objects.filter(cashflow=cashflow)
        serializer = DailyInflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DailyInflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class DailyOutflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = Cashflow.objects.filter(cashflow=cashflow)
        serializer = DailyOutflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DailyOutflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

# weekly sheets

class WeeklyInflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = WeeklyInflow.objects.filter(cashflow=cashflow)
        serializer = WeeklyInflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WeeklyInflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class WeeklyOutflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = WeeklyOutflow.objects.filter(cashflow=cashflow)
        serializer = WeeklyOutflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WeeklyOutflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

# monthly sheets

class MonthlyInflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = MonthlyInflow.objects.filter(cashflow=cashflow)
        serializer = MonthlyInflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MonthlyInflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class MonthlyOutflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = MonthlyOutflow.objects.filter(cashflow=cashflow)
        serializer = MonthlyOutflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MonthlyOutflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

# quarterly sheets

class QuarterlyInflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = QuarterlyInflow.objects.filter(cashflow=cashflow)
        serializer = QuarterlyInflowSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuarterlyInflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class QuarterlyOutflowView(APIView):
    def get(self, request, format=None):
        cashflow = self.request.query_params.get('cashflow', None)
        sheet = Cashflow.objects.filter(cashflow=cashflow)
        serializer = QuarterlyOutflow(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuarterlyOutflowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)
