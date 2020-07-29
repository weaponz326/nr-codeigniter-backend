from django.shortcuts import render
from django.contrib.auth.models import User
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from allauth.account.signals import user_signed_up
from allauth.account.admin import EmailAddress

from .models import Profile
from .serializers import ProfileStoreSerializer, ProfileSerializer


# Create your views here.

# stores first user form in a session to be inserted after second user form    
class ProfileStoreView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProfileStoreSerializer(data=request.data)
        if serializer.is_valid():
            request.session['first_name'] = request.data.get('first_name')
            request.session['last_name'] = request.data.get('last_name')
            request.session['location'] = request.data.get('location')
            request.session['about'] = request.data.get('about')
            return Response({'status': True})
        else:
            return Response({'status': False})

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class PollVerificationView(APIView):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.session['user_id'])
        email = EmailAddress.objects.filter(user=user, verified=True)
        if email.exists():
            return Response({'ver_status': True})
        else:
            return Response({'ver_status': False})

# use email to get user to be verified and assign to session
class VerificationEmailView(APIView):
    def post(self, request, *args, **kwargs):
        email = User.objects.filter(email=request.data.get('email'))
        if email.exists():
            user = User.objects.get(email=request.data.get('email'))
            request.session['user_id'] = user.id
            return Response({'status': True})
        else:
            return Response({'status': False})

# check if user is looged in
class LoginStatusView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response(
                {
                    'logged_in': True,
                    'id': request.user.id,
                    'name': request.user.first_name
                }
            )
        else:
            return Response({'logged_in': False})


# update user with session values after account reistration
@receiver(user_signed_up)
def insert_session_receiver(request, sender, user, **kwargs):
    # update user model with firstname and lastname
    account = User(first_name=request.session['first_name'], last_name=request.session['last_name'])
    account.id = user.id
    account.save(update_fields=['first_name', 'last_name'])

    # insert location and about into profile
    profile = Profile(user=user, location=request.session['location'], about=request.session['about'])
    profile.save()

    # save user to session
    request.session['user_id'] = user.id


