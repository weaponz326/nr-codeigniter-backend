from django.urls import path, include
from . import views


urlpatterns = [
    path('service/', views.ServiceView.as_view()),
    path('service/<int:pk>', views.ServiceDetailView.as_view()),
    path('service-item/', views.ServiceItemView.as_view()),
    path('service-item/<int:pk>', views.ServiceItemDetailView.as_view()),
]