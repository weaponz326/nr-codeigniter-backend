from django.urls import path, include
from . import views


urlpatterns = [
    path('room/', views.RoomView.as_view()),
    path('room/<int:pk>', views.RoomDetailView.as_view()),
]