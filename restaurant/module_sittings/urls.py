from django.urls import path, include
from . import views


urlpatterns = [
    path('sitting/', views.SittingView.as_view()),
    path('sitting-list/', views.SittingListView.as_view()),
    path('sitting/<int:pk>', views.SittingDetailView.as_view()),
]