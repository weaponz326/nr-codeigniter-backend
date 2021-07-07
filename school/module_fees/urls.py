from django.urls import path, include
from . import views


urlpatterns = [
    path('fees/', views.FeeView.as_view()),
    path('fees/<int:pk>', views.FeeDetailView.as_view()),
    path('target-class/', views.TargetClassView.as_view()),
    path('target-class/<int:pk>', views.TargetClassDetailView.as_view()),
    path('fees-item/', views.FeesItemView.as_view()),
    path('fees-item/<int:pk>', views.FeesItemDetailView.as_view()),
    path('arrears-item/', views.ArrearsItemView.as_view()),
    path('arrears-item/<int:pk>', views.ArrearsItemDetailView.as_view()),
    path('generate-bill/', views.GenerateBillView.as_view()),
    path('bill/', views.BillView.as_view()),
    path('bill/<int:pk>', views.BillDetailView.as_view()),
    path('student-bill/', views.StudentBillView.as_view()),
    path('bill-arrears/', views.BillArrearsView.as_view()),
]