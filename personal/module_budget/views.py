from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Budget, Income, Expenditure
from .serializers import BudgetSerializer, IncomeSerializer, ExpenditureSerializer


# Create your views here.

class BudgetView(APIView):
    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        budget = Budget.objects.filter(user=user)
        serializer = BudgetSerializer(budget, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class BudgetDetailView(APIView):
    def get(self, request, pk, format=None):
        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        budget = Budget.objects.get(pk=pk)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        budget = Budget.objects.get(pk=pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# income
# --------------------------------------------------------------------------------------------------

class IncomeView(APIView):
    def get(self, request, format=None):
        budget = self.request.query_params.get('budget', None)
        income = Income.objects.filter(budget=budget)
        serializer = IncomeSerializer(income, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class IncomeDetailView(APIView):
    def get(self, request, pk, format=None):
        income = Income.objects.get(pk=pk)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        income = Income.objects.get(pk=pk)
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        income = Income.objects.get(pk=pk)
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# income
# --------------------------------------------------------------------------------------------------

class ExpenditureView(APIView):
    def get(self, request, format=None):
        budget = self.request.query_params.get('budget', None)
        expenditure = Expenditure.objects.filter(budget=budget)
        serializer = ExpenditureSerializer(expenditure, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenditureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ExpenditureDetailView(APIView):
    def get(self, request, pk, format=None):
        expenditure = Expenditure.objects.get(pk=pk)
        serializer = ExpenditureSerializer(expenditure)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        expenditure = Expenditure.objects.get(pk=pk)
        serializer = ExpenditureSerializer(expenditure, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        expenditure = Expenditure.objects.get(pk=pk)
        expenditure.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
