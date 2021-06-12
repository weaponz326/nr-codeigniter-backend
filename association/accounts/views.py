from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics

from .models import Profile
from .serializers import ProfileSerializer, UserAccountsSerializer
from module_admin.models import User


# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# creates a new association profile and add creator to personal users
class NewProfileView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            profile = Profile(
                name=request.data.get("name"),
                location=request.data.get("location"),
                about=request.data.get("about")
            )
            profile.save()

            # personal users in admin module
            user = User(
                personal_id=request.user.id,
                account=Profile.objects.latest("id"),
                is_creator=True,
                is_admin=True
            )
            user.save()

            return Response({'status': True})
        else:
            return Response(
                {
                    'status': False,
                    'errors': serializer.errors
                }
            )
            
# checks if user has a association acount
class HasAccountView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(personal_id=request.user.id)
        if user.exists():
            return Response({'has_account': True})
        else:
            return Response({'has_account': False})

# store user selected active account in session
class ActiveAccountView(APIView):
    def post(self, request, *args, **kwargs):
        request.session['active'] = True
        request.session['association_id'] = request.data.get('active_account')
        
        return Response(
            {
                'active': request.session['active'],
                'association_id': request.session['association_id']
            }
        )

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'active': request.session['active'],
                'association_id': request.session['association_id']
            }
        )

# get all association suites of a personal id
class UserAccountsView(generics.ListAPIView):
    serializer_class = UserAccountsSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        personal_id = self.request.query_params.get('personal_id', None)
        if personal_id is not None:
            queryset = queryset.filter(personal_id=personal_id)
        return queryset
        