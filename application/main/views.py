from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

# gets user source from request url and store it in a session for redirection
class UserSourceView(APIView):
    def post(self, request, *args, **kwargs):
        request.session['user_source'] = request.data.get('user_source')
        return Response({'user_source': request.session['user_source']})

    def get(self, request, *args, **kwargs):
        return Response({'user_source': request.session['user_source']})
