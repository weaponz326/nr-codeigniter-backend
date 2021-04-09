from django.urls import path, include
from . import views


urlpatterns = [
    path('payment/', views.PaymentView.as_view()),
    path('payment-list/', views.PaymentListView.as_view()),
    path('payment/<int:pk>', views.PaymentDetailView.as_view()),
]