from django.urls import path, include
from . import views


urlpatterns = [
    path('subject/', views.SubjectView.as_view()),
    path('subject-list/', views.SubjectListView.as_view()),
    path('subject/<int:pk>', views.SubjectDetailView.as_view()),
]