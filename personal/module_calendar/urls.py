from django.urls import path, include
from . import views


urlpatterns = [
    path('appointment/', views.AppointmentView.as_view()),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view()),
    path('appointment-list', views.AppointmentListView.as_view()),
]
