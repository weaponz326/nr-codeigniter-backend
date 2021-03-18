from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Timetable
from accounts.models import Profile
from module_terms.models import Term
from .serializers import TimetableSerializer


# Create your views here.

class TimetableView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = TimetableSerializer
        queryset = Timetable.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = TimetableSerializer(data=request.data)
        if serializer.is_valid():
            timetable = Timetable(
                account=Profile.objects.get(id=request.data.get("school_id")),
                timetable_code=request.data.get("timetable_code"),
                timetable_name=request.data.get("timetable_name"),
                timetable_date=request.data.get("timetable_date"),
            )
            timetable.save()
            latest_timetable = Timetable.objects.latest("id")

            return Response({
                'status': True,
                'timetable_id': latest_timetable.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class TimetableListView(generics.ListAPIView):
    serializer_class = TimetableSerializer

    def get_queryset(self):
        queryset = Timetable.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class TimetableDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
