from django.urls import path, include
from . import views


urlpatterns = [
    path('class/', views.ClassView.as_view()),
    path('class/<int:pk>', views.ClassDetailView.as_view()),
    path('class-subject/', views.ClassSubjectView.as_view()),
    path('class-subject/<int:pk>/', views.ClassSubjectDetailView.as_view()),
]