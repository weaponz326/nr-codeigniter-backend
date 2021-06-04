from django.urls import path, include
from . import views


urlpatterns = [
    path('order/', views.OrderView.as_view()),
    path('order/<int:pk>', views.OrderDetailView.as_view()),
]