from django.urls import path, include
from . import views


urlpatterns = [
    path('received/', views.ReceivedView.as_view()),
    path('received/<int:pk>', views.ReceivedDetailView.as_view()),
    path('sent/', views.SentView.as_view()),
    path('sent/<int:pk>', views.SentDetailView.as_view()),
]