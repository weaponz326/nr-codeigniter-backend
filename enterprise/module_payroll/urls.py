from django.urls import path, include
from . import views


urlpatterns = [
    path('payroll/', views.PayrollView.as_view()),
    path('payroll/<int:pk>', views.PayrollDetailView.as_view()),
]
