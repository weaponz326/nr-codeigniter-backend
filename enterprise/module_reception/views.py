from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Visitor
from accounts.models import Profile
from .serializers import VisitorSerializer


# Create your views here.

class VisitorView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = VisitorSerializer
        queryset = Visitor.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            visitor = Visitor(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                visit_code=request.data.get("visit_code"),
                visit_date=request.data.get("visit_date"),
                visitor_name=request.data.get("visitor_name"),
                visitor_phone=request.data.get("visitor_phone"),
                arrival=request.data.get("arrival"),
                departure=request.data.get("departure"),
                purpose=request.data.get("purpose"),
                tag_number=request.data.get("tag_number"),
            )
            visitor.save()
            latest_visitor = Visitor.objects.latest("id")

            return Response({
                'status': True,
                'visitor_id': latest_visitor.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class VisitorListView(generics.ListAPIView):
    serializer_class = VisitorSerializer

    def get_queryset(self):
        queryset = Visitor.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class VisitorDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
