from django.urls import path, include
from . import views


urlpatterns = [
    path('invoice/', views.InvoiceView.as_view()),
    path('invoice/<int:pk>', views.InvoiceDetailView.as_view()),
    path('invoice-item/', views.InvoiceItemView.as_view()),
    path('invoice-item/<int:pk>', views.InvoiceItemDetailView.as_view()),
]