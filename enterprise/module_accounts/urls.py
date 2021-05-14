from django.urls import path, include
from . import views


urlpatterns = [
    path('account/', views.AccountView.as_view()),
    path('account/<int:pk>', views.AccountDetailView.as_view()),
    path('transaction/', views.TransactionView.as_view()),
    path('transaction/<int:pk>', views.TransactionDetailView.as_view()),
    path('all-transactions/', views.AllTransactionsView.as_view()),
]
