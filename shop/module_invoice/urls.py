from django.urls import path, include
from . import views


urlpatterns = [
    path('invoice/', views.InvoiceView.as_view()),
    path('invoice-list/', views.InvoiceListView.as_view()),
    path('invoice/<int:pk>', views.InvoiceDetailView.as_view()),
]