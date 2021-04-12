from django.urls import path, include
from . import views


urlpatterns = [
    path('payable/', views.PayableView.as_view()),
    path('payable-list/', views.PayableListView.as_view()),
    path('payable/<int:pk>', views.PayableDetailView.as_view()),
]