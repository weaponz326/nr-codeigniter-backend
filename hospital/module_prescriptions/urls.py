from django.urls import path, include
from . import views


urlpatterns = [
    path('new-prescription/', views.NewPrescriptionView.as_view()),
    path('prescription/', views.PrescriptionView.as_view()),
    path('prescription-list/', views.PrescriptionListView.as_view()),
    path('prescription/<int:pk>', views.PrescriptionDetailView.as_view()),
    path('detail/', views.DetailView.as_view()),
    path('detail-list/', views.DetailListView.as_view()),
    path('detail/<int:pk>', views.DetailDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
    path('doctor-list/', views.DoctorListView.as_view()),
]