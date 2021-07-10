from django.urls import path, include
from . import views


urlpatterns = [
    path('dues/', views.DuesView.as_view()),
    path('dues/<int:pk>', views.DuesDetailView.as_view()),
    path('dues-payment/', views.DuesPaymentView.as_view()),
    path('dues-payment/<int:pk>', views.DuesPaymentDetailView.as_view()),
]