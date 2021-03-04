from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import User, Access, Activity
from .serializers import UserSerializer, AccessSerializer, ActivitySerializer


# Create your views here.

# users
# --------------------------------------------------------------

class UserView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer
        queryset = User.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        view = AccessView.as_view()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User(
                hospital=Profile.objects.get(id=request.data.get("hospital_id")),
                personal_id=request.data.get("personal_id"),
                is_creator=request.data.get("is_creator"),
                is_admin=request.data.get("is_admin"),
                is_manager=request.data.get("is_manager"),
            )
            user.save()
            latest_user = User.objects.latest("id")

            # call user access

            return view(requset, *args, **kwargs)
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class UserDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# access
# -------------------------------------------------------------------

class AccessView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AccessSerializer
        queryset = Access.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            access = Access(
                user=Profile.objects.get(id=request.data.get("user")),
                admin_access=request.data.get("admin_access"),
                admissions_access=request.data.get("admissions_access"),
                appointments_access=request.data.get("appointments_access"),
                bills_access=request.data.get("bills_access"),
                diagnosis_access=request.data.get("diagnosis_access"),
                dispensary_access=request.data.get("dispensary_access"),
                doctors_access=request.data.get("doctors_access"),
                drugs_access=request.data.get("drugs_access"),
                laboratory_access=request.data.get("laboratory_access"),
                nurses_access=request.data.get("nurses_access"),
                patients_access=request.data.get("patients_access"),
                payments_access=request.data.get("payments_access"),
                portal_access=request.data.get("portal_access"),
                prescriptions_access=request.data.get("prescriptions_access"),
                settings_access=request.data.get("settings_access"),
                staff_access=request.data.get("staff_access"),
                wards_access=request.data.get("wards_access"),
            )
            access.id = request.date.get("user_id")
            access.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AccessListView(generics.ListAPIView):
    serializer_class = AccessSerializer

    def get_queryset(self):
        queryset = Access.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital=hospital)
        return queryset

class AccessDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Access.objects.all()
    serializer_class = AccessSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# activity
# --------------------------------------------------------------------

class ActivityView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ActivitySerializer
        queryset = Activity.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            activity = Activity(
                user=Activity.objects.get(id=request.data.get("user")),
                time=request.data.get("time"),
                activity_module=request.data.get("activity_module"),
                description=request.data.get("description"),
            )
            activity.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class UserActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class AllActivityListView(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = User.objects.all()
        hospital = self.request.query_params.get('user', None)
        if hospital is not None:
            queryset = queryset.filter(hospital__hospital=hospital)
        return queryset
