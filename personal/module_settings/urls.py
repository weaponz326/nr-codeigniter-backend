from django.urls import path, include
from . import views


urlpatterns = [
    path('profile-user/<int:pk>', views.ProfileUserView.as_view()),
    path('user/<int:pk>', views.UserView.as_view()),
    path('profile/<int:pk>', views.ProfileView.as_view()),
    path('additional-profile/<int:pk>', views.AdditionalProfileDetailView.as_view()),
    path('location-details/<int:pk>', views.LocationDetailsDetailView.as_view()),
    path('additional-profile/', views.AdditionalProfileView.as_view()),
    path('location-details/', views.LocationDetailsView.as_view()),
]
