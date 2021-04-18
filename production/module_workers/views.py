from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Worker
from accounts.models import Profile
from .serializers import WorkerSerializer, WorkerListSerializer


# Create your views here.

class WorkerView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = WorkerSerializer
        queryset = Worker.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            worker = Worker(
                account=Profile.objects.get(id=request.data.get("production_id")),
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                sex=request.data.get("sex"),
                date_of_birth=request.data.get("date_of_birth"),
                nationality=request.data.get("nationality"),
                religion=request.data.get("religion"),
                phone=request.data.get("phone"),
                email=request.data.get("email"),
                address=request.data.get("address"),
                state=request.data.get("state"),
                city=request.data.get("city"),
                post_code=request.data.get("post_code"),
                worker_code=request.data.get("worker_code"),
                department=request.data.get("department"),
                speciality=request.data.get("speciality"),
                job=request.data.get("job"),
            )
            worker.save()
            latest_worker = Worker.objects.latest("id")

            return Response({
                'status': True,
                'worker_id': latest_worker.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class WorkerListView(generics.ListAPIView):
    serializer_class = WorkerListSerializer

    def get_queryset(self):
        queryset = Worker.objects.all()
        production = self.request.query_params.get('user', None)
        if production is not None:
            queryset = queryset.filter(account=production)
        return queryset

class WorkerDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
