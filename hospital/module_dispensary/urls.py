from django.urls import path, include
from . import views


urlpatterns = [
    path('dispensary/', views.DispensaryView.as_view()),
    path('dispensary/<int:pk>', views.DispensaryDetailView.as_view()),
    path('dispensary-drug/', views.DispensaryDrugView.as_view()),
    path('dispensary-drug/<int:pk>', views.DispensaryDrugDetailView.as_view()),
]