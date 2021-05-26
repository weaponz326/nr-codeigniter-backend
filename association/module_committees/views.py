from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Committee, CommitteeMember
from .serializers import CommitteeSerializer, CommitteeMemberSerializer, CommitteeMemberListSerializer


# Create your views here.

class CommitteeView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        committee = Committee.objects.filter(account=account)
        serializer = CommitteeSerializer(committee, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommitteeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class CommitteeDetailView(APIView):
    def get(self, request, pk, format=None):
        committee = Committee.objects.get(pk=pk)
        serializer = CommitteeSerializer(committee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        committee = Committee.objects.get(pk=pk)
        serializer = CommitteeSerializer(committee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        committee = Committee.objects.get(pk=pk)
        committee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# committee members
# -----------------------------------------------------------------------------------------------------------

class CommitteeMemberView(APIView):
    def get(self, request, format=None):
        committee = self.request.query_params.get('committee', None)
        member = CommitteeMember.objects.filter(committee=committee)
        serializer = CommitteeMemberListSerializer(member, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommitteeMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class CommitteeMemberDetailView(APIView):
    def get(self, request, pk, format=None):
        member = CommitteeMember.objects.get(pk=pk)
        serializer = CommitteeMemberListSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        member = CommitteeMember.objects.get(pk=pk)
        serializer = CommitteeMemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        member = CommitteeMember.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
