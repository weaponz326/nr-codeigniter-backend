from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink-list/', views.RinkListView.as_view()),
    path('search/', views.SearchListView.as_view()),
    path('search-detail/<int:pk>', views.SearchDetailView.as_view()),
    path('admission-list', views.AdmissionListView.as_view()),
    path('patient-list', views.PatientListView.as_view()),
    path('doctor-list', views.DoctorListView.as_view()),
    path('nurse-list', views.NurseListView.as_view()),
    path('rink/<int:pk>', views.RinkDetailView.as_view()),
    path('admission/<int:pk>', views.AdmissionDetailView.as_view()),
    path('patient/<int:pk>', views.PatientDetailView.as_view()),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view()),
    path('nurse/<int:pk>', views.NurseDetailView.as_view()),
]
