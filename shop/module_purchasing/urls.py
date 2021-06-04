from django.urls import path, include
from . import views


urlpatterns = [
    path('purchasing/', views.PurchasingView.as_view()),
    path('purchasing/<int:pk>', views.PurchasingDetailView.as_view()),
    path('purchasing-item/', views.PurchasingItemView.as_view()),
    path('purchasing-item/<int:pk>', views.PurchasingItemDetailView.as_view()),
]