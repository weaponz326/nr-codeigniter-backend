from django.urls import path, include
from . import views


urlpatterns = [
    path('supplier/', views.SupplierView.as_view()),
    path('supplier-list/', views.SupplierListView.as_view()),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view()),
]