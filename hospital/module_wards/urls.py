from django.urls import path, include
from . import views


urlpatterns = [
    path('ward/', views.WardView.as_view()),
    path('ward/<int:pk>', views.WardDetailView.as_view()),
    path('ward-patient/', views.WardPatientView.as_view()),
    path('ward-patient/<int:pk>', views.WardPatientDetailView.as_view()),
]