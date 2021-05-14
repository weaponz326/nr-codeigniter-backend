from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Appraisal
from .serializers import AppraisalSerializer, AppraisalListSerializer


# Create your views here.

class AppraisalView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        appraisal = Appraisal.objects.filter(account=account)
        serializer = AppraisalListSerializer(appraisal, many=True)        
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
        serializer = AppraisalListSerializer(appraisal)
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
