from django.urls import path, include
from . import views


urlpatterns = [
    path('diagnosis/', views.DiagnosisView.as_view()),
    path('diagnosis/<int:pk>', views.DiagnosisDetailView.as_view()),
]