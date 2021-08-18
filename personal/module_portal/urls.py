from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink/<int:pk>', views.RinkDetailView.as_view()),
    path('rink-list/', views.RinkListView.as_view()),
    path('search/', views.SearchListView.as_view()),
    path('search/<int:pk>', views.SearchDetailView.as_view()),
]
