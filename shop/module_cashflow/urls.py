from django.urls import path, include
from . import views


urlpatterns = [
    path('sheet/', views.CashflowView.as_view()),
    path('sheet/<int:pk>', views.CashflowDetailView.as_view()),
    path('daily-inflow/', views.DailyInflowView.as_view()),
    path('daily-outflow/', views.DailyOutflowView.as_view()),
    path('weekly-inflow/', views.WeeklyInflowView.as_view()),
    path('weekly-outflow/', views.WeeklyOutflowView.as_view()),
    path('monthly-inflow/', views.MonthlyInflowView.as_view()),
    path('monthly-outflow/', views.MonthlyOutflowView.as_view()),
    path('quarterly-inflow/', views.QuarterlyInflowView.as_view()),
    path('quarterly-outflow/', views.QuarterlyOutflowView.as_view()),
]