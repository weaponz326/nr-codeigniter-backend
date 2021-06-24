from django.urls import path, include
from . import views


urlpatterns = [
    path('bill/', views.BillView.as_view()),
    path('bill/<int:pk>', views.BillDetailView.as_view()),
    path('general/', views.GeneralView.as_view()),
    path('general/<int:pk>', views.GeneralDetailView.as_view()),
    path('appointment/', views.AppointmentChargeView.as_view()),
    path('appointment/<int:pk>', views.AppointmentChargeDetailView.as_view()),
    path('lab/', views.LaboratoryChargeView.as_view()),
    path('lab/<int:pk>', views.LaboratoryChargeDetailView.as_view()),
    path('dispensary/', views.DispensaryChargeView.as_view()),
    path('dispensary/<int:pk>', views.DispensaryChargeDetailView.as_view()),
    path('ward/', views.WardChargeView.as_view()),
    path('ward/<int:pk>', views.WardChargeDetailView.as_view()),
]