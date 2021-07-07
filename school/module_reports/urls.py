from django.urls import path, include
from . import views


urlpatterns = [
    path('report/', views.ReportView.as_view()),
    path('report/<int:pk>', views.ReportDetailView.as_view()),
    path('report-assessment/', views.ReportAssessmentView.as_view()),
    path('refresh-sheet/', views.RefreshSheetView.as_view()),
    path('class-report-student/', views.ClassReportStudentView.as_view()),
    path('class-sheet/', views.ClassAssessmentSheetView.as_view()),
    path('student-report/', views.StudentReportView.as_view()),
    path('student-sheet/', views.StudentAssessmentSheetView.as_view()),
]