from django.urls import path, include
from . import views


urlpatterns = [
    path('new-diagnosis/', views.NewDiagnosisView.as_view()),
    path('diagnosis/', views.DiagnosisView.as_view()),
    path('diagnosis-list/', views.DiagnosisListView.as_view()),
    path('diagnosis/<int:pk>', views.DiagnosisDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
    path('doctor-list/', views.DoctorListView.as_view()),
]