from django.urls import path, include
from . import views


urlpatterns = [
    path('new-payment/', views.NewPaymentView.as_view()),
    path('payment/', views.PaymentView.as_view()),
    path('payment-list/', views.PaymentListView.as_view()),
    path('payment/<int:pk>', views.PaymentDetailView.as_view()),
    path('patient-list/', views.PatientListView.as_view()),
    path('admission-list/', views.AdmissionListView.as_view()),
    path('bill-list/', views.BillListView.as_view()),
]