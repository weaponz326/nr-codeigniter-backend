from django.urls import path, include
from . import views


urlpatterns = [
    path('term/', views.TermView.as_view()),
    path('term-list/', views.TermListView.as_view()),
    path('term/<int:pk>', views.TermDetailView.as_view()),
]