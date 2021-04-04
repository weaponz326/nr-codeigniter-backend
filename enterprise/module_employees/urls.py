from django.urls import path, include
from . import views


urlpatterns = [
    path('employee/', views.EmployeeView.as_view()),
    path('employee-list/', views.EmployeeListView.as_view()),
    path('employee/<int:pk>', views.EmployeeDetailView.as_view()),
]