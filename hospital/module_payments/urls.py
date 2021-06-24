from django.urls import path, include
from . import views


urlpatterns = [
    path('payment/', views.PaymentView.as_view()),
    path('payment/<int:pk>', views.PaymentDetailView.as_view()),
    path('payments-history/', views.PaymentsHistoryView.as_view()),
]