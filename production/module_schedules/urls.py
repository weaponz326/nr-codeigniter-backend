from django.urls import path, include
from . import views


urlpatterns = [
    path('schedule/', views.ScheduleView.as_view()),
    path('schedule-list/', views.ScheduleListView.as_view()),
    path('schedule/<int:pk>', views.ScheduleDetailView.as_view()),
]