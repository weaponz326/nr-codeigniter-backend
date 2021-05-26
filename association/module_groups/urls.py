from django.urls import path, include
from . import views


urlpatterns = [
    path('group/', views.GroupView.as_view()),
    path('group/<int:pk>', views.GroupDetailView.as_view()),
    path('group-member/', views.GroupMemberView.as_view()),
    path('group-member/<int:pk>', views.GroupMemberDetailView.as_view()),
]