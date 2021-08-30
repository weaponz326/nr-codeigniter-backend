from django.urls import path, include

from . import views


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('user-profile/', views.UserProfileView.as_view()),

    # for settings
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user-profile/<int:pk>', views.UserProfileDetailView.as_view()),

    path('search/', views.SearchListView.as_view()),
    path('search/<int:pk>', views.SearchDetailView.as_view()),
]
