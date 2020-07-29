from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('profile', views.ProfileView)

urlpatterns = [
    path('new-profile/', views.NewProfileView.as_view()),
    path('has-account/', views.HasAccountView.as_view()),
    path('user-accounts/', views.UserAccountsView.as_view()),
    path('active-account/', views.ActiveAccountView.as_view()),

    path('', include(router.urls)),
]