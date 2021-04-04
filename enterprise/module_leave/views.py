from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Leave
from accounts.models import Profile
from .serializers import LeaveSerializer


# Create your views here.

class LeaveView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = LeaveSerializer
        queryset = Leave.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = LeaveSerializer(data=request.data)
        if serializer.is_valid():
            leave = Leave(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                leave_code=request.data.get("leave_code"),
                date_requested=request.data.get("date_requested"),
                leave_type=request.data.get("leave_type"),
                from_date=request.data.get("from_date"),
                to_date=request.data.get("to_date"),
                reason=request.data.get("reason"),
                status=request.data.get("status"),
            )
            leave.save()
            latest_leave = Leave.objects.latest("id")

            return Response({
                'status': True,
                'leave_id': latest_leave.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class LeaveListView(generics.ListAPIView):
    serializer_class = LeaveSerializer

    def get_queryset(self):
        queryset = Leave.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class LeaveDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
