from django.urls import path, include
from . import views


urlpatterns = [
    path('new-bill/', views.NewBillView.as_view()),
    path('bill/', views.BillView.as_view()),
    path('bill-list/', views.BillListView.as_view()),
    path('bill/<int:pk>', views.BillDetailView.as_view()),
    path('order-list/', views.OrderListView.as_view()),
    path('sitting-list/', views.SittingListView.as_view()),
    path('delivery-list/', views.DeliveryListView.as_view()),
]