from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Member
from .serializers import MemberSerializer, MemberListSerializer


# Create your views here.

class MemberView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        member = Member.objects.filter(account=account)
        serializer = MemberListSerializer(member, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class MemberDetailView(APIView):
    def get(self, request, pk, format=None):
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        member = Member.objects.get(pk=pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        member = Member.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

