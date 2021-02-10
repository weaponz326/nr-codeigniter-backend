from django.urls import path, include
from . import views


urlpatterns = [
    path('stock-item/', views.StockItemView.as_view()),
    path('stock-item-list/', views.StockItemListView.as_view()),
    path('stock-item/<int:pk>', views.StockItemDetailView.as_view()),
]