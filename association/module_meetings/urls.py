from django.urls import path, include
from . import views


urlpatterns = [
    path('meeting/', views.MeetingView.as_view()),
    path('meeting/<int:pk>', views.MeetingDetailView.as_view()),
]