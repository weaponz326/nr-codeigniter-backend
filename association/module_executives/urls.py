from django.urls import path, include
from . import views


urlpatterns = [
    path('executive/', views.ExecutiveView.as_view()),
    path('executive/<int:pk>', views.ExecutiveDetailView.as_view()),
]