from django.urls import path, include
from . import views


urlpatterns = [
    path('reservation/', views.ReservationView.as_view()),
    path('reservation/<int:pk>', views.ReservationDetailView.as_view()),
]