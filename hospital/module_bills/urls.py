from django.urls import path, include
from . import views


urlpatterns = [
    path('bill/', views.BillView.as_view()),
    path('bill/<int:pk>', views.BillDetailView.as_view()),
    path('general/', views.GeneralView.as_view()),
    path('general/<int:pk>', views.GeneralDetailView.as_view()),
]