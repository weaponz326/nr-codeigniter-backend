from django.urls import path, include
from . import views


urlpatterns = [
    path('extended-profile/', views.ExtendedProfileView.as_view()),
    path('extended-profile/<int:pk>', views.ExtendedProfileDetailView.as_view()),
    path('subscription/', views.SubscriptionView.as_view()),
    path('subscription/<int:pk>', views.SubscriptionDetailView.as_view()),
]
