from django.urls import path, include
from . import views


urlpatterns = [
    path('folder/', views.FolderView.as_view()),
    path('folder-list/', views.FolderListView.as_view()),
    path('folder/<int:pk>', views.FolderDetailView.as_view()),
    path('file/', views.FileView.as_view()),
    path('file-list/', views.FileListView.as_view()),
    path('file/<int:pk>', views.FileDetailView.as_view()),
]