from django.urls import path, include
from . import views


urlpatterns = [
    path('attendance/', views.AttendanceView.as_view()),
    path('attendance-list/', views.AttendanceListView.as_view()),
    path('attendance/<int:pk>', views.AttendanceDetailView.as_view()),
]