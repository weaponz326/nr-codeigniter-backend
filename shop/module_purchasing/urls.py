from django.urls import path, include
from . import views


urlpatterns = [
    path('purchasing/', views.PurchasingView.as_view()),
    path('purchasing-list/', views.PurchasingListView.as_view()),
    path('purchasing/<int:pk>', views.PurchasingDetailView.as_view()),
]