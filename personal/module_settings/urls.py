from django.urls import path, include
from . import views


urlpatterns = [
    path('settings-profile/', views.SettingsProfileView.as_view()),
    path('settings-profile/<int:pk>', views.SettingsProfileDetailView.as_view()),
    path('user-profile/<int:pk>', views.ProfileDetailView.as_view()),
]
