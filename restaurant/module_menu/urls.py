from django.urls import path, include
from . import views


urlpatterns = [
    path('menu-item/', views.MenuItemView.as_view()),
    path('menu-item-list/', views.MenuItemListView.as_view()),
    path('menu-item/<int:pk>', views.MenuItemDetailView.as_view()),
]