from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user-list/', views.UserListView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    # path('access/', views.AccessView.as_view()),
    path('access-list/', views.AccessListView.as_view()),
    path('access/<int:pk>', views.AccessDetailView.as_view()),
    path('activity/', views.ActivityView.as_view()),
    path('user-activity-list/', views.UserActivityListView.as_view()),
    path('all-activity-list/', views.AllActivityListView.as_view()),
]