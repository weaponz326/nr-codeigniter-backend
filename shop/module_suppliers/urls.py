from django.urls import path, include
from . import views


urlpatterns = [
    path('supplier/', views.SupplierView.as_view()),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view()),
    path('supplier-product/', views.SupplierProductView.as_view()),
    path('supplier-product/<int:pk>', views.SupplierProductDetailView.as_view()),
]