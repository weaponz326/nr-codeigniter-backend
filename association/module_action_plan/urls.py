from django.urls import path, include
from . import views


urlpatterns = [
    path('plan/', views.PlanView.as_view()),
    path('plan/<int:pk>', views.PlanDetailView.as_view()),
    path('plan-step/', views.StepView.as_view()),
    path('plan-step/<int:pk>', views.StepDetailView.as_view()),
]
