from django.urls import path, include
from . import views


urlpatterns = [
    path('prescription/', views.PrescriptionView.as_view()),
    path('prescription/<int:pk>', views.PrescriptionDetailView.as_view()),
    path('detail/', views.DetailView.as_view()),
    path('detail/<int:pk>', views.DetailDetailView.as_view()),
]