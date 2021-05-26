from django.urls import path, include
from . import views


urlpatterns = [
    path('member/', views.MemberView.as_view()),
    path('member/<int:pk>', views.MemberDetailView.as_view()),
]