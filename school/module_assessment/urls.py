from django.urls import path, include
from . import views


urlpatterns = [
    path('assessment/', views.AssessmentView.as_view()),
    path('assessment/<int:pk>', views.AssessmentDetailView.as_view()),
    path('refresh-sheet/', views.RefreshSheetView.as_view()),
    path('class-sheet/', views.ClassSheetView.as_view()),
]