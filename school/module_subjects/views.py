from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Subject
from accounts.models import Profile
from module_terms.models import Term
from .serializers import SubjectSerializer


# Create your views here.

class SubjectView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = SubjectSerializer
        queryset = Subject.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            subject = Subject(
                account=Profile.objects.get(id=request.data.get("school_id")),
                # term=Term.objects.get(id=request.data.get("term")),
                subject_code=request.data.get("subject_code"),
                subject_name=request.data.get("subject_name"),
                department=request.data.get("department"),
                description=request.data.get("description"),
            )
            subject.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class SubjectListView(generics.ListAPIView):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class SubjectDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
