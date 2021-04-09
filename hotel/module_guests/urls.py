from django.urls import path, include
from . import views


urlpatterns = [
    path('guest/', views.GuestView.as_view()),
    path('guest-list/', views.GuestListView.as_view()),
    path('guest/<int:pk>', views.GuestDetailView.as_view()),
]