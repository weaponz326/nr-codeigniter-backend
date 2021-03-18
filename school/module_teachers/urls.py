from django.urls import path, include
from . import views


urlpatterns = [
    path('teacher/', views.TeacherView.as_view()),
    path('teacher-list/', views.TeacherListView.as_view()),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view()),
]