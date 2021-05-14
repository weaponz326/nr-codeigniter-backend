from django.urls import path, include
from . import views


urlpatterns = [
    path('appraisal/', views.AppraisalView.as_view()),
    path('appraisal/<int:pk>', views.AppraisalDetailView.as_view()),
]