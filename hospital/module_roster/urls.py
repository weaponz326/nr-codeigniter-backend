from django.urls import path, include
from . import views


urlpatterns = [
    path('roster/', views.RosterView.as_view()),
    path('roster/<int:pk>', views.RosterDetailView.as_view()),
    path('shift/', views.ShiftView.as_view()),
    path('shift/<int:pk>', views.ShiftDetailView.as_view()),
    path('batch/', views.BatchView.as_view()),
    path('batch/<int:pk>', views.BatchDetailView.as_view()),
    path('refresh-personnel/', views.RefreshPersonnelView.as_view()),
]