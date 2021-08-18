from django.urls import path, include
from . import views


urlpatterns = [
    path('note/', views.NoteView.as_view()),
    path('note/<int:pk>', views.NoteDetailView.as_view()),
    # path('subject/', views.SubjectView.as_view()),
    # path('body/', views.BodyView.as_view()),
    path('file/', views.FileView.as_view()),
]
