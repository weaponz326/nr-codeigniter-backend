from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Asset
from accounts.models import Profile
from .serializers import AssetSerializer


# Create your views here.

class AssetView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AssetSerializer
        queryset = Asset.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            asset = Asset(
                account=Profile.objects.get(id=request.data.get("hotel_id")),
                asset_code=request.data.get("asset_code"),
                asset_name=request.data.get("asset_name"),
                asset_type=request.data.get("asset_type"),
                category=request.data.get("category"),
                brand=request.data.get("brand"),
                model=request.data.get("model"),
                purchased_date=request.data.get("purchased_date"),
                location=request.data.get("location"),
                description=request.data.get("description"),
                condition=request.data.get("condition"),
            )
            asset.save()
            latest_asset = Asset.objects.latest("id")

            return Response({
                'status': True,
                'asset_id': latest_asset.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AssetListView(generics.ListAPIView):
    serializer_class = AssetSerializer

    def get_queryset(self):
        queryset = Asset.objects.all()
        hotel = self.request.query_params.get('user', None)
        if hotel is not None:
            queryset = queryset.filter(account=hotel)
        return queryset

class AssetDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
