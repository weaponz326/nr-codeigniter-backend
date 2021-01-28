from django.urls import path, include
from . import views


urlpatterns = [
    path('new-dispensary/', views.NewDispensaryView.as_view()),
    path('dispensary/', views.DispensaryView.as_view()),
    path('dispensary-list/', views.DispensaryListView.as_view()),
    path('dispensary/<int:pk>', views.DispensaryDetailView.as_view()),
    path('detail/', views.DetailView.as_view()),
    path('detail-list/', views.DetailListView.as_view()),
    path('detail/<int:pk>', views.DetailDetailView.as_view()),
    path('prescription-list/', views.PrescriptionListView.as_view()),
]