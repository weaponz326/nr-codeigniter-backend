from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink-list/', views.RinkListView.as_view()),
    path('search/', views.SearchListView.as_view()),
    path('search-detail/<int:pk>', views.SearchDetailView.as_view()),
    # path('student-list', views.StudentListView.as_view()),
    # path('teacher-list', views.TeacherListView.as_view()),
    # path('subject-list', views.SubjectListView.as_view()),
    path('rink/<int:pk>', views.RinkDetailView.as_view()),
    # path('student/<int:pk>', views.StudentDetailView.as_view()),
    # path('teacher/<int:pk>', views.TeacherDetailView.as_view()),
    # path('subject/<int:pk>', views.SubjectDetailView.as_view()),
]
