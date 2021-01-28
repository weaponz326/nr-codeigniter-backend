from django.urls import path, include
from . import views


urlpatterns = [
    path('ward/', views.WardView.as_view()),
    path('ward-list/', views.WardListView.as_view()),
    path('ward/<int:pk>', views.WardDetailView.as_view()),
    path('new-ward-patient/', views.WardPatientSaveView.as_view()),
    path('ward-patient-list/', views.WardPatientListView.as_view()),
    path('ward-patient/<int:pk>', views.WardPatientDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
]