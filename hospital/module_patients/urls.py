from django.urls import path, include
from . import views


urlpatterns = [
    path('patient/', views.PatientView.as_view()),
    path('patient/<int:pk>', views.PatientDetailView.as_view()),
]