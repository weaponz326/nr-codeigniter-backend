from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Report
from accounts.models import Profile
from module_terms.models import Term
from module_classes.models import Class
from .serializers import ReportSerializer, ReportListSerializer


# Create your views here.

class ReportView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = ReportSerializer
        queryset = Report.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report = Report(
                account=Profile.objects.get(id=request.data.get("school_id")),
                clas=Class.objects.get(id=request.data.get("clas")),
                report_code=request.data.get("report_code"),
                report_name=request.data.get("report_name"),
                report_date=request.data.get("report_date"),
            )
            report.save()

            return Response({ 'status': True })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class ReportListView(generics.ListAPIView):
    serializer_class = ReportListSerializer

    def get_queryset(self):
        queryset = Report.objects.all()
        school = self.request.query_params.get('user', None)
        if school is not None:
            queryset = queryset.filter(account=school)
        return queryset

class ReportDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
