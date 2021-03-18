from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Term
from accounts.models import Profile
from .serializers import TermSerializer


# Create your views here.

class TermView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = TermSerializer
        queryset = Term.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = TermSerializer(data=request.data)
        if serializer.is_valid():
            term = Term(
                account=Profile.objects.get(id=request.data.get("school_id")),
                term_name=request.data.get("term_name"),
                term_begins=request.data.get("term_begins"),
                term_ends=request.data.get("term_ends"),
                academic_year=request.data.get("academic_year"),
                term_status=request.data.get("term_status"),
            )
            term.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class TermListView(generics.ListAPIView):
    serializer_class = TermSerializer

    def get_queryset(self):
        queryset = Term.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class TermDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Term.objects.all()
    serializer_class = TermSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
