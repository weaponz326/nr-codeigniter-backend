from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('profile', views.ProfileView)

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    
    path('password-reset/confirm/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
    
    path('profile-store/', views.ProfileStoreView.as_view()),
    path('poll-verification/', views.PollVerificationView.as_view()),
    path('login-status/', views.LoginStatusView.as_view()),
    
    path('', include(router.urls)),
]
