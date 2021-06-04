from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Worker
from .serializers import WorkerSerializer, WorkerListSerializer


# Create your views here.

class WorkerView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        worker = Worker.objects.filter(account=account)
        serializer = WorkerListSerializer(worker, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class WorkerDetailView(APIView):
    def get(self, request, pk, format=None):
        worker = Worker.objects.get(pk=pk)
        serializer = WorkerSerializer(worker)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        worker = Worker.objects.get(pk=pk)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        worker = Worker.objects.get(pk=pk)
        worker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
