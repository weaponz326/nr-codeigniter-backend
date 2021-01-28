from django.urls import path, include
from . import views


urlpatterns = [
    path('new-lab/', views.NewLaboratoryView.as_view()),
    path('lab/', views.LaboratoryView.as_view()),
    path('lab-list/', views.LaboratoryListView.as_view()),
    path('lab/<int:pk>', views.LaboratoryDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
    path('doctor-list/', views.DoctorListView.as_view()),
]