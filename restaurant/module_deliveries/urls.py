from django.urls import path, include
from . import views


urlpatterns = [
    path('delivery/', views.DeliveryView.as_view()),
    path('delivery-list/', views.DeliveryListView.as_view()),
    path('delivery/<int:pk>', views.DeliveryDetailView.as_view()),
    path('order-list/', views.OrderListView.as_view()),
]