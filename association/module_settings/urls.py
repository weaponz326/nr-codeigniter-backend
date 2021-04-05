from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/<int:pk>', views.ProfileDetailView.as_view()),
    path('extended-profile/<int:pk>', views.ExtendedProfileDetailView.as_view()),
    path('location-extended/', views.LocationExtendedView.as_view()),
    path('contact-extended/', views.ContactExtendedView.as_view()),
]
