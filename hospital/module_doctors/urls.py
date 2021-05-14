from django.urls import path, include
from . import views


urlpatterns = [
    path('doctor/', views.DoctorView.as_view()),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view()),
]