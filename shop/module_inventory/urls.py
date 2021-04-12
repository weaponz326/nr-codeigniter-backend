from django.urls import path, include
from . import views


urlpatterns = [
    path('inventory/', views.InventoryItemView.as_view()),
    path('inventory-list/', views.InventoryItemListView.as_view()),
    path('inventory/<int:pk>', views.InventoryItemDetailView.as_view()),
]