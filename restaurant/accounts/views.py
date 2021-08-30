from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins, status
from rest_framework import filters
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer, UserAccountsSerializer
from module_admin.models import User


# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# class ProfileView(APIView):
#     def get(self, request, format=None):
#         account = self.request.query_params.get('account', None)
#         profile = Profile.objects.filter(account=account)
#         serializer = ProfileSerializer(profile, many=True)        
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({ 'message': 'OK', 'data': serializer.data })
#         return Response(serializer.errors)

# class ProfileDetailView(APIView):
#     def get(self, request, pk, format=None):
#         profile = Profile.objects.get(pk=pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         profile = Profile.objects.get(pk=pk)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({ 'message': 'OK', 'data': serializer.data })
#         return Response(serializer.errors)

#     def delete(self, request, pk, format=None):
#         profile = Profile.objects.get(pk=pk)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# creates a new restaurant profile and add creator to personal users

# -----------------------------------------------------------------------------------------------

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
                personal_id=request.data.get("personal_id"),
                account=Profile.objects.latest("id"),
                user_level='Admin',
                is_creator=True,
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

# checks if user has a restaurant acount
class HasAccountView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(personal_id=request.data.get('personal_id'))
        if user.exists():
            return Response({'has_account': True})
        else:
            return Response({'has_account': False})

# store user selected active account in session
class ActiveAccountView(APIView):
    def post(self, request, *args, **kwargs):
        request.session['active'] = True
        request.session['restaurant_id'] = request.data.get('active_account')
        
        return Response(
            {
                'active': request.session['active'],
                'restaurant_id': request.session['restaurant_id']
            }
        )

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'active': request.session['active'],
                'restaurant_id': request.session['restaurant_id']
            }
        )

# get all restaurant suites of a personal id
class UserAccountsView(generics.ListAPIView):
    serializer_class = UserAccountsSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        personal_id = self.request.query_params.get('personal_id', None)
        if personal_id is not None:
            queryset = queryset.filter(personal_id=personal_id)
        return queryset
        
# --------------------------------------------------------------------------------------------------------

# restaurant search
class SearchListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
class SearchDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
