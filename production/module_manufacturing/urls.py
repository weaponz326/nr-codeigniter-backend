from django.urls import path, include
from . import views


urlpatterns = [
    path('manufacturing/', views.ManufacturingView.as_view()),
    path('manufacturing/<int:pk>', views.ManufacturingDetailView.as_view()),
]