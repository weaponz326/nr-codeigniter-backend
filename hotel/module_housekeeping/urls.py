from django.urls import path, include
from . import views


urlpatterns = [
    path('housekeeping/', views.HousekeepingView.as_view()),
    path('housekeeping-list/', views.HousekeepingListView.as_view()),
    path('housekeeping/<int:pk>', views.HousekeepingDetailView.as_view()),
    # path('checklist/', views.ChecklistView.as_view()),
    # path('checklist-list/', views.ChecklistListView.as_view()),
    # path('checklist/<int:pk>', views.ChecklistDetailView.as_view()),
]