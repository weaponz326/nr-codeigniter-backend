from django.urls import path, include
from . import views


urlpatterns = [
    path('section/', views.SectionView.as_view()),
    path('section/<int:pk>', views.SectionDetailView.as_view()),
]