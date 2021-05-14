from django.urls import path, include
from . import views


urlpatterns = [
    path('assessment/', views.AssessmentView.as_view()),
    path('assessment/<int:pk>', views.AssessmentDetailView.as_view()),
]