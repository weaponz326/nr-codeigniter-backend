from django.urls import path, include
from . import views


urlpatterns = [
    path('admission/', views.AdmissionView.as_view()),
    path('admission/<int:pk>', views.AdmissionDetailView.as_view()),
]