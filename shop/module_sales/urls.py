from django.urls import path, include
from . import views


urlpatterns = [
    path('sales/', views.SalesView.as_view()),
    path('sales-list/', views.SalesListView.as_view()),
    path('sales/<int:pk>', views.SalesDetailView.as_view()),
]