from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink-list/', views.RinkListView.as_view()),
    path('search/', views.SearchListView.as_view()),
    path('search-detail/<int:pk>', views.SearchDetailView.as_view()),
    path('task-list', views.TaskListView.as_view()),
    path('appointment-list', views.AppointmentListView.as_view()),
    path('note-list', views.NoteListView.as_view()),
    path('rink/<int:pk>', views.RinkDetailView.as_view()),
    path('task/<int:pk>', views.TaskDetailView.as_view()),
    path('appointment/<int:pk>', views.AppointmentDetailView.as_view()),
    path('note/<int:pk>', views.NoteDetailView.as_view()),
]
