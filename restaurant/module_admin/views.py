from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User, Access, Invitation
from .serializers import UserSerializer, AccessSerializer, InvitationSerializer


# Create your views here.

# users

class UserView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        user = User.objects.filter(account=account)
        serializer = UserSerializer(user, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class UserDetailView(APIView):
    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# access
# ---------------------------------------------------------------------------

class AccessView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        access = Access.objects.filter(account=account)
        serializer = AccessSerializer(access, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AccessDetailView(APIView):
    def get(self, request, pk, format=None):
        access = Access.objects.get(pk=pk)
        serializer = AccessSerializer(access)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        access = Access.objects.get(pk=pk)
        serializer = AccessSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        access = Access.objects.get(pk=pk)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------------------------

class InvitationView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        invitation = Invitation.objects.filter(account=account)
        serializer = InvitationSerializer(invitation, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class InvitationDetailView(APIView):
    def get(self, request, pk, format=None):
        invitation = Invitation.objects.get(pk=pk)
        serializer = InvitationSerializer(invitation)
        # r = requests.get('localhost:8001/' . serializer.data.personal_id)
        # TODO: join reqest response with serailizer data
        return Response(serializer.data)
