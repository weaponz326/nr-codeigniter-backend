from django.urls import path, include
from . import views


urlpatterns = [
    path('report/', views.ReportView.as_view()),
    path('report-list/', views.ReportListView.as_view()),
    path('report/<int:pk>', views.ReportDetailView.as_view()),
]