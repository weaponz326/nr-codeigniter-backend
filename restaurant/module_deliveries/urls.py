from django.urls import path, include
from . import views


urlpatterns = [
    path('delivery/', views.DeliveryView.as_view()),
    path('delivery/<int:pk>', views.DeliveryDetailView.as_view()),
]