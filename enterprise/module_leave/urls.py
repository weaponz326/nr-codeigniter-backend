from django.urls import path, include
from . import views


urlpatterns = [
    path('leave/', views.LeaveView.as_view()),
    path('leave-list/', views.LeaveListView.as_view()),
    path('leave/<int:pk>', views.LeaveDetailView.as_view()),
]