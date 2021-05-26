from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Group, GroupMember
from .serializers import GroupSerializer, GroupMemberSerializer, GroupMemberListSerializer


# Create your views here.

class GroupView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        group = Group.objects.filter(account=account)
        serializer = GroupSerializer(group, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class GroupDetailView(APIView):
    def get(self, request, pk, format=None):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# group members
# -----------------------------------------------------------------------------------------------------------

class GroupMemberView(APIView):
    def get(self, request, format=None):
        group = self.request.query_params.get('group', None)
        member = GroupMember.objects.filter(group=group)
        serializer = GroupMemberListSerializer(member, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class GroupMemberDetailView(APIView):
    def get(self, request, pk, format=None):
        member = GroupMember.objects.get(pk=pk)
        serializer = GroupMemberListSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        member = GroupMember.objects.get(pk=pk)
        serializer = GroupMemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        member = GroupMember.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
