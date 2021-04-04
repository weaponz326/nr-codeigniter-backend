from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Budget, Income, Expenditure
from accounts.models import Profile
from .serializers import BudgetSerializer, IncomeSerializer, ExpenditureSerializer


# Create your views here.

class BudgetView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = BudgetSerializer
        queryset = Budget.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            budget = Budget(
                account=Profile(id=request.data.get("user")),
                budget_name=request.data.get("budget_name"),
                budget_type=request.data.get("budget_type")
            )
            budget.save()
            latest_budget = Budget.objects.latest("id")
            
            return Response({
                'status': True,
                'budget_id': latest_budget.id
            })
        else:
            return Response({'status': False})

class BudgetListView(generics.ListAPIView):
    serializer_class = BudgetSerializer

    def get_queryset(self):
        queryset = Budget.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class BudgetDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# income

class IncomeListView(generics.ListAPIView):
    serializer_class = IncomeSerializer

    def get_queryset(self):
        queryset = Income.objects.all()
        budget = self.request.query_params.get('budget', None)
        if budget is not None:
            queryset = queryset.filter(budget=budget)
        return queryset

class IncomeView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IncomeDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# expenditure

class ExpenditureListView(generics.ListAPIView):
    serializer_class = ExpenditureSerializer

    def get_queryset(self):
        queryset = Expenditure.objects.all()
        budget = self.request.query_params.get('budget', None)
        if budget is not None:
            queryset = queryset.filter(budget=budget)
        return queryset

class ExpenditureView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ExpenditureDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
