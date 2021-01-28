from django.urls import path, include
from . import views


urlpatterns = [
    path('new-bill/', views.NewBillView.as_view()),
    path('bill/', views.BillView.as_view()),
    path('bill-list/', views.BillListView.as_view()),
    path('bill/<int:pk>', views.BillDetailView.as_view()),
    path('general/', views.GeneralView.as_view()),
    path('general-list/', views.GeneralListView.as_view()),
    path('general/<int:pk>', views.GeneralDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
    path('admission-list/', views.AdmissionListView.as_view()),
]