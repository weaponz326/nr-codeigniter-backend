from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from .models import Appraisal
from accounts.models import Profile
from .serializers import AppraisalSerializer


# Create your views here.

class AppraisalView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AppraisalSerializer
        queryset = Appraisal.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AppraisalSerializer(data=request.data)
        if serializer.is_valid():
            appraisal = Appraisal(
                account=Profile.objects.get(id=request.data.get("enteprise_id")),
                appraisal_code=request.data.get("appraisal_code"),
                start_date=request.data.get("start_date"),
                end_date=request.data.get("end_date"),
                supervisor=request.data.get("supervisor"),
                description=request.data.get("description"),
            )
            appraisal.save()
            latest_appraisal = Appraisal.objects.latest("id")

            return Response({
                'status': True,
                'appraisal_id': latest_appraisal.id
            })
        else:
            return Response({ 'status': False, 'errors': serializer.errors })

class AppraisalListView(generics.ListAPIView):
    serializer_class = AppraisalSerializer

    def get_queryset(self):
        queryset = Appraisal.objects.all()
        enterprise = self.request.query_params.get('user', None)
        if enterprise is not None:
            queryset = queryset.filter(account=enterprise)
        return queryset

class AppraisalDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
