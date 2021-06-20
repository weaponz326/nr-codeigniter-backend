from django.urls import path, include
from . import views


urlpatterns = [
    path('attendance/', views.AttendanceView.as_view()),
    path('attendance/<int:pk>', views.AttendanceDetailView.as_view()),
    path('refresh-sheet/', views.RefreshSheetView.as_view()),
    path('attendance-config/', views.AttendanceConfigView.as_view()),
    path('attendance-sheet/', views.AttendanceSheetView.as_view())
]