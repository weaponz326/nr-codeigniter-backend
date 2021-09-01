from django.urls import path, include
from . import views


urlpatterns = [
    path('note/', views.NoteView.as_view()),
    path('note/<int:pk>', views.NoteDetailView.as_view()),
    path('file/', views.NoteFileView.as_view()),
    path('file/<int:pk>', views.NoteFileDetailView.as_view()),
]
