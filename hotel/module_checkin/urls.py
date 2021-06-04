from django.urls import path, include
from . import views


urlpatterns = [
    path('checkin/', views.CheckinView.as_view()),
    path('checkin/<int:pk>', views.CheckinDetailView.as_view()),
]