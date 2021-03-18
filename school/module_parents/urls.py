from django.urls import path, include
from . import views


urlpatterns = [
    path('parent/', views.ParentView.as_view()),
    path('parent-list/', views.ParentListView.as_view()),
    path('parent/<int:pk>', views.ParentDetailView.as_view()),
    path('student-list/', views.StudentListView.as_view()),
    path('ward/', views.ParentWardView.as_view()),
    path('ward-list/', views.ParentWardListView.as_view()),
    path('ward/<int:pk>', views.ParentWardDetailView.as_view()),
]