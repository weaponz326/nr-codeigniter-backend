from django.urls import path, include
from . import views


urlpatterns = [
    path('drug/', views.DrugView.as_view()),
    path('drug/<int:pk>', views.DrugDetailView.as_view()),
]