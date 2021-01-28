from django.urls import path, include
from . import views


urlpatterns = [
    path('admission/', views.AdmissionView.as_view()),
    path('admission-list/', views.AdmissionListView.as_view()),
    path('admission/<int:pk>', views.AdmissionDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
]