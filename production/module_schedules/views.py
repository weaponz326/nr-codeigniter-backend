from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Schedule, ScheduleItem
from accounts.models import Profile
from .serializers import ScheduleSerializer


# Create your views here.

class ScheduleView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ScheduleSerializer
        queryset = Schedule.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            schedule = Schedule(
                account=Profile.objects.get(id=request.data.get("production_id")),
                schedule_name=request.data.get("schedule_name"),
                schedule_code=request.data.get("schedule_code"),
                from_date=request.data.get("from_date"),
                to_date=request.data.get("to_date"),
            )
            schedule.save()
            latest_schedule = Schedule.objects.latest("id")

            return Response({
                'status': True,
                'schedule_id': latest_schedule.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ScheduleListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Schedule.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class ScheduleDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
