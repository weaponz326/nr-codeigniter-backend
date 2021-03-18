from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Assessment
from accounts.models import Profile
from module_terms.models import Term
from module_subjects.models import Subject
from .serializers import AssessmentSerializer, AssessmentListSerializer


# Create your views here.

class AssessmentView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AssessmentSerializer
        queryset = Assessment.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            assessment = Assessment(
                account=Profile.objects.get(id=request.data.get("school_id")),
                subject=Subject.objects.get(id=request.data.get("subject")),
                assessment_code=request.data.get("assessment_code"),
                assessment_name=request.data.get("assessment_name"),
                assessment_date=request.data.get("assessment_date"),
            )
            assessment.save()
            latest_assessment = Assessment.objects.latest("id")

            return Response({
                'status': True,
                'asssessment_id': latest_assessment.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AssessmentListView(generics.ListAPIView):
    serializer_class = AssessmentListSerializer

    def get_queryset(self):
        queryset = Assessment.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class AssessmentDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
