from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Report
from .serializers import ReportSerializer


# Create your views here.

class ReportView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        report = Report.objects.filter(account=account)
        serializer = ReportSerializer(report, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ReportDetailView(APIView):
    def get(self, request, pk, format=None):
        report = Report.objects.get(pk=pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        report = Report.objects.get(pk=pk)
        serializer = ReportSerializer(report, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        report = Report.objects.get(pk=pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
