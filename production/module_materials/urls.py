from django.urls import path, include
from . import views


urlpatterns = [
    path('material/', views.MaterialView.as_view()),
    path('material/<int:pk>', views.MaterialDetailView.as_view()),
]