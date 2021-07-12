from django.urls import path, include
from . import views


urlpatterns = [
    path('order/', views.OrderView.as_view()),
    path('order/<int:pk>', views.OrderDetailView.as_view()),
    path('order-item/', views.OrderItemView.as_view()),
    path('order-item/<int:pk>', views.OrderItemDetailView.as_view()),
    path('order-item/<int:pk>', views.OrderItemDetailView.as_view()),
]