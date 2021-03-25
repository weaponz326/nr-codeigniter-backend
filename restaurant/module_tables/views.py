from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Table
from accounts.models import Profile
from .serializers import TableSerializer


# Create your views here.

class TableView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = TableSerializer
        queryset = Table.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            table = Table(
                account=Profile.objects.get(id=request.data.get("restaurant_id")),
                table_number=request.data.get("table_number"),
                table_type=request.data.get("table_type"),
                capacity=request.data.get("capacity"),
                location=request.data.get("location"),
                table_status=request.data.get("table_status"),
            )
            table.save()
            latest_table = Table.objects.latest("id")

            return Response({
                'status': True,
                'table_id': latest_table.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class TableListView(generics.ListAPIView):
    serializer_class = TableSerializer

    def get_queryset(self):
        queryset = Table.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(account=restaurant)
        return queryset

class TableDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
