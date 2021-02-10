from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import MenuItem
from accounts.models import Profile
from .serializers import MenuItemSerializer


# Create your views here.

class MenuItemView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = MenuItemSerializer
        queryset = MenuItem.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            menu = MenuItem(
                restaurant=Profile.objects.get(id=request.data.get("restaurant_id")),
                item_code=request.data.get("item_code"),
                item_name=request.data.get("item_name"),
                category=request.data.get("category"),
                price=request.data.get("price"),
                description=request.data.get("description"),
            )
            menu.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class MenuItemListView(generics.ListAPIView):
    serializer_class = MenuItemSerializer

    def get_queryset(self):
        queryset = MenuItem.objects.all()
        restaurant = self.request.query_params.get('user', None)
        if restaurant is not None:
            queryset = queryset.filter(restaurant=restaurant)
        return queryset

class MenuItemDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
