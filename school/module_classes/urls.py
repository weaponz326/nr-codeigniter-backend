from django.urls import path, include
from . import views


urlpatterns = [
    path('class/', views.ClassView.as_view()),
    path('class-list/', views.ClassListView.as_view()),
    path('class/<int:pk>', views.ClassDetailView.as_view()),
    path('all-subjects-list/', views.AllSubjectListView.as_view()),
    path('class-subject-list/', views.ClassSubjectListView.as_view()),
]