from django.urls import path, include
from . import views


urlpatterns = [
    path('fees/', views.FeeView.as_view()),
    path('fees/<int:pk>', views.FeeDetailView.as_view()),
    path('fees-item/', views.FeesItemView.as_view()),
    path('fees-item/<int:pk>', views.FeesItemDetailView.as_view()),
]