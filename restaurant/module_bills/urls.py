from django.urls import path, include
from . import views


urlpatterns = [
    path('bill/', views.BillView.as_view()),
    path('bill/<int:pk>', views.BillDetailView.as_view()),
]