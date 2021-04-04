from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Ledger, LedgerItem
from accounts.models import Profile
from .serializers import LedgerSerializer, LedgerItemSerializer


# Create your views here.

# ledger

class LedgerView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = LedgerSerializer
        queryset = Ledger.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = LedgerSerializer(data=request.data)
        if serializer.is_valid():
            ledger = Ledger(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                ledger_code=request.data.get("ledger_code"),
                ledger_date=request.data.get("ledger_date"),
                ledger_name=request.data.get("ledger_name"),
                from_date=request.data.get("from_date"),
                to_date=request.data.get("to_date"),
            )
            ledger.save()
            latest_ledger = Ledger.objects.latest("id")

            return Response({
                'status': True,
                'ledger_id': latest_ledger.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class LedgerListView(generics.ListAPIView):
    serializer_class = LedgerSerializer

    def get_queryset(self):
        queryset = Ledger.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class LedgerDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# ------------------------------------------------------------------------------------

# ledger items

class LedgerItemView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = LedgerItemSerializer
        queryset = LedgerItem.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = LedgerItemSerializer(data=request.data)
        if serializer.is_valid():
            item = LedgerItem(
                ledger=Ledger.objects.get(id=request.data.get("ledger")),
                item_date=request.data.get("item_date"),
                reference=request.data.get("reference"),
                item_type=request.data.get("item_type"),
                details=request.data.get("details"),
                amount=request.data.get("amount"),
            )
            item.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class LedgerItemListView(generics.ListAPIView):
    serializer_class = LedgerItemSerializer

    def get_queryset(self):
        queryset = LedgerItem.objects.all()
        ledger = self.request.query_params.get('ledger', None)
        if ledger is not None:
            queryset = queryset.filter(ledger=ledger)
        return queryset

class LedgerItemDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = LedgerItem.objects.all()
    serializer_class = LedgerItemSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
