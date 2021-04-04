from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Received, Sent
from accounts.models import Profile
from .serializers import ReceivedSerializer, SentSerializer


# Create your views here.


# received letters
# -------------------------------------------------------------------------------------------

class ReceivedView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ReceivedSerializer
        queryset = Received.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ReceivedSerializer(data=request.data)
        if serializer.is_valid():
            received = Received(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                reference_number=request.data.get("reference_number"),
                letter_date=request.data.get("letter_date"),
                sender=request.data.get("sender"),
                subject=request.data.get("subject"),
                date_received=request.data.get("date_received")
            )
            received.save()
            latest_received = Received.objects.latest("id")

            return Response({
                'status': True,
                'received_id': latest_received.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ReceivedListView(generics.ListAPIView):
    serializer_class = ReceivedSerializer

    def get_queryset(self):
        queryset = Received.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class ReceivedDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Received.objects.all()
    serializer_class = ReceivedSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# sent letters
# -------------------------------------------------------------------------------------------

class SentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SentSerializer
        queryset = Sent.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = SentSerializer(data=request.data)
        if serializer.is_valid():
            sent = Sent(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                reference_number=request.data.get("reference_number"),
                letter_date=request.data.get("letter_date"),
                recipient=request.data.get("recipient"),
                subject=request.data.get("subject"),
                date_received=request.data.get("date_received")
            )
            sent.save()
            latest_sent = Sent.objects.latest("id")

            return Response({
                'status': True,
                'sent_id': latest_sent.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class SentListView(generics.ListAPIView):
    serializer_class = SentSerializer

    def get_queryset(self):
        queryset = Sent.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class SentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Sent.objects.all()
    serializer_class = SentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
