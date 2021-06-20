from django.urls import path, include
from . import views


urlpatterns = [
    path('roster/', views.RosterView.as_view()),
    path('roster/<int:pk>', views.RosterDetailView.as_view()),
]