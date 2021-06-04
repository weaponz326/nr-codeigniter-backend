from django.urls import path, include
from . import views


urlpatterns = [
    path('receivable/', views.ReceivableView.as_view()),
    path('receivable/<int:pk>', views.ReceivableDetailView.as_view()),
]