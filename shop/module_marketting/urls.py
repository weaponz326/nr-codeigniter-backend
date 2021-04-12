from django.urls import path, include
from . import views


urlpatterns = [
    path('campaign/', views.CampaignView.as_view()),
    path('campaign-list/', views.CampaignListView.as_view()),
    path('campaign/<int:pk>', views.CampaignDetailView.as_view()),
]