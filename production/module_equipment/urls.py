from django.urls import path, include
from . import views


urlpatterns = [
    path('equipment/', views.EquipmentView.as_view()),
    path('equipment-list/', views.EquipmentListView.as_view()),
    path('equipment/<int:pk>', views.EquipmentDetailView.as_view()),
]