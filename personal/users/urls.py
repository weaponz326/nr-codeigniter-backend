from django.urls import path, include

from . import views


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('user-profile/', views.UserProfileView.as_view()),
]
