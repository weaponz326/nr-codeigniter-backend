from django.urls import path, include
from . import views


urlpatterns = [
    path('budget/', views.BudgetView.as_view()),
    path('budget-list/', views.BudgetListView.as_view()),
    path('budget/<int:pk>', views.BudgetDetailView.as_view()),
    path('income-list/', views.IncomeListView.as_view()),
    path('income/', views.IncomeView.as_view()),
    path('income/<int:pk>', views.IncomeDetailView.as_view()),
    path('expenditure-list/', views.ExpenditureListView.as_view()),
    path('expenditure/', views.ExpenditureView.as_view()),
    path('expenditure/<int:pk>', views.ExpenditureDetailView.as_view()),
]
