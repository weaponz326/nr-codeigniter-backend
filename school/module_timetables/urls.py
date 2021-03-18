from django.urls import path, include
from . import views


urlpatterns = [
    path('timetable/', views.TimetableView.as_view()),
    path('timetable-list/', views.TimetableListView.as_view()),
    path('timetable/<int:pk>', views.TimetableDetailView.as_view()),
]