from django.urls import path, include
from . import views


urlpatterns = [
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.BookingDetailView.as_view()),
    path('booked-room/', views.BookedRoomView.as_view()),
    path('booked-room/<int:pk>', views.BookedRoomDetailView.as_view()),
]