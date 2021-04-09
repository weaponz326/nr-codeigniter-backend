from django.urls import path, include
from . import views


urlpatterns = [
    path('service/', views.ServiceView.as_view()),
    path('service-list/', views.ServiceListView.as_view()),
    path('service/<int:pk>', views.ServiceDetailView.as_view()),
]