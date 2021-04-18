from django.urls import path, include
from . import views


urlpatterns = [
    path('worker/', views.WorkerView.as_view()),
    path('worker-list/', views.WorkerListView.as_view()),
    path('worker/<int:pk>', views.WorkerDetailView.as_view()),
]