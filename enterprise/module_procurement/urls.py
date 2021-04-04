from django.urls import path, include
from . import views


urlpatterns = [
    path('procurement/', views.ProcurementView.as_view()),
    path('procurement-list/', views.ProcurementListView.as_view()),
    path('procurement/<int:pk>', views.ProcurementDetailView.as_view()),
]