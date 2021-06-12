from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import UserSerializer, UserProfileSerializer


# Create your views here.
class UserProfileView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # update user model with firstname and lastname
            user = User(first_name=request.data.get('first_name'), last_name=request.data.get('last_name'))
            user.id = request.user.id
            user.save(update_fields=['first_name', 'last_name'])

            # insert location and about into profile
            profile = Profile(user=user, location=request.data.get('location'), about=request.data.get('about'))
            profile.id = request.user.id
            profile.save()

            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)
        

