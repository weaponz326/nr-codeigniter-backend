from django.urls import path, include
from . import views


urlpatterns = [
    path('nurse/', views.NurseView.as_view()),
    path('nurse/<int:pk>', views.NurseDetailView.as_view()),
]