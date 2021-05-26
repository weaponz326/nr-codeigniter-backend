from django.urls import path, include
from . import views


urlpatterns = [
    path('committee/', views.CommitteeView.as_view()),
    path('committee/<int:pk>', views.CommitteeDetailView.as_view()),
    path('committee-member/', views.CommitteeMemberView.as_view()),
    path('committee-member/<int:pk>', views.CommitteeMemberDetailView.as_view()),
]