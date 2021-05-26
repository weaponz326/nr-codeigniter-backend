from django.urls import path, include
from . import views


urlpatterns = [
    path('year/', views.YearView.as_view()),
    path('year/<int:pk>', views.YearDetailView.as_view()),
]