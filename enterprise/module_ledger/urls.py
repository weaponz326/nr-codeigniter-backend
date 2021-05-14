from django.urls import path, include
from . import views


urlpatterns = [
    path('ledger/', views.LedgerView.as_view()),
    path('ledger/<int:pk>', views.LedgerDetailView.as_view()),
    path('ledger-item/', views.LedgerItemView.as_view()),
    path('ledger-item/<int:pk>', views.LedgerItemDetailView.as_view()),
]