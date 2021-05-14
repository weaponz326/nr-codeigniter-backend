from django.urls import path, include
from . import views


urlpatterns = [
    path('visitor/', views.VisitorView.as_view()),
    path('visitor/<int:pk>', views.VisitorDetailView.as_view()),
]