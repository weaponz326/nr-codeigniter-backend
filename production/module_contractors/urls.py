from django.urls import path, include
from . import views


urlpatterns = [
    path('contractor/', views.ContractorView.as_view()),
    path('contractor/<int:pk>', views.ContractorDetailView.as_view()),
]