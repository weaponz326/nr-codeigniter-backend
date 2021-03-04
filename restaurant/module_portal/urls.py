from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink-list/', views.RinkListView.as_view()),
    path('search/', views.SearchListView.as_view()),
    path('search-detail/<int:pk>', views.SearchDetailView.as_view()),
    path('staff-list', views.StaffListView.as_view()),
    path('customer-list', views.CustomerListView.as_view()),
    path('menu-list', views.MenuListView.as_view()),
    path('rink/<int:pk>', views.RinkDetailView.as_view()),
    path('staff/<int:pk>', views.StaffDetailView.as_view()),
    path('customer/<int:pk>', views.CustomerDetailView.as_view()),
    path('menu/<int:pk>', views.MenuDetailView.as_view()),
]
