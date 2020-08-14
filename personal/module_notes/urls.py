from django.urls import path, include
from . import views


urlpatterns = [
    path('subject/', views.SubjectView.as_view()),
    path('body/', views.BodyView.as_view()),
    path('note-list', views.NoteListView.as_view()),
]
