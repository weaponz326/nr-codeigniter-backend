from django.urls import path, include
from . import views


urlpatterns = [
    path('customer/', views.CustomerView.as_view()),
    path('customer-list/', views.CustomerListView.as_view()),
    path('customer/<int:pk>', views.CustomerDetailView.as_view()),
]