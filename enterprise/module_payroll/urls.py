from django.urls import path, include
from . import views


urlpatterns = [
    path('payroll/', views.PayrollView.as_view()),
    path('payroll/<int:pk>', views.PayrollDetailView.as_view()),
    path('payroll-sheet/', views.PayrollSheetView.as_view()),
    path('payroll-sheet/<int:pk>', views.PayrollSheetDetailView.as_view()),
    path('refresh-sheet/', views.RefreshSheetView.as_view()),
]
