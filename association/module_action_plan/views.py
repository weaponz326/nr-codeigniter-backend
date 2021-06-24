from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Plan, Step
from .serializers import PlanSerializer, StepSerializer


# Create your views here.

class PlanView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        plan = Plan.objects.filter(account=account)
        serializer = PlanSerializer(plan, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class PlanDetailView(APIView):
    def get(self, request, pk, format=None):
        plan = Plan.objects.get(pk=pk)
        serializer = PlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        plan = Plan.objects.get(pk=pk)
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        plan = Plan.objects.get(pk=pk)
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# steps

class StepView(APIView):
    def get(self, request, format=None):
        plan = self.request.query_params.get('plan', None)
        step = Step.objects.filter(plan=plan)
        serializer = StepSerializer(step, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StepSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class StepDetailView(APIView):
    def get(self, request, pk, format=None):
        step = Step.objects.get(pk=pk)
        serializer = StepSerializer(step)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        step = Step.objects.get(pk=pk)
        serializer = StepSerializer(step, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        step = Step.objects.get(pk=pk)
        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
