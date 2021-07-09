from django.urls import path, include
from . import views


urlpatterns = [
    path('attendance/', views.AttendanceView.as_view()),
    path('attendance/<int:pk>', views.AttendanceDetailView.as_view()),
    path('refresh-sheet/', views.RefreshSheetView.as_view()),
    path('attendance-day/', views.AttendanceDayView.as_view()),
    path('attendance-employee/', views.AttendanceStudentView.as_view()),
    path('attendance-check/', views.AttendanceCheckView.as_view()),
    path('attendance-check/<int:pk>', views.AttendanceCheckDetailView.as_view()),
]