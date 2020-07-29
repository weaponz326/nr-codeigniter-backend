from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('profile', views.ProfileView)

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('profile-store/', views.ProfileStoreView.as_view()),
    path('poll-verification/', views.PollVerificationView.as_view()),
    path('verification-email/', views.VerificationEmailView.as_view()),
    path('login-status/', views.LoginStatusView.as_view()),
    
    path('', include(router.urls)),
]
