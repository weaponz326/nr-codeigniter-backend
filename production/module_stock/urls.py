from django.urls import path, include
from . import views


urlpatterns = [
    path('stock/', views.StockItemView.as_view()),
    path('stock/<int:pk>', views.StockItemDetailView.as_view()),
]