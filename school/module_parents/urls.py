from django.urls import path, include
from . import views


urlpatterns = [
    path('parent/', views.ParentView.as_view()),
    path('parent/<int:pk>', views.ParentDetailView.as_view()),
    path('parent-ward/', views.ParentWardView.as_view()),
    path('parent-ward/<int:pk>', views.ParentWardDetailView.as_view()),
]