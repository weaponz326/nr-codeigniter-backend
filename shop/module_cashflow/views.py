from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Sheet
from accounts.models import Profile
from .serializers import SheetSerializer


# Create your views here.

class SheetView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SheetSerializer
        queryset = Sheet.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = SheetSerializer(data=request.data)
        if serializer.is_valid():
            sheet = Sheet(
                account=Profile.objects.get(id=request.data.get("shop_id")),
                sheet_code=request.data.get("sheet_code"),
                sheet_name=request.data.get("sheet_name"),
                sheet_type=request.data.get("sheet_type"),
            )
            sheet.save()
            latest_sheet = Sheet.objects.latest("id")

            return Response({
                'status': True,
                'sheet_id': latest_sheet.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class SheetListView(generics.ListAPIView):
    serializer_class = SheetSerializer

    def get_queryset(self):
        queryset = Sheet.objects.all()
        shop = self.request.query_params.get('user', None)
        if shop is not None:
            queryset = queryset.filter(account=shop)
        return queryset

class SheetDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
