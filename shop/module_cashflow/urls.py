from django.urls import path, include
from . import views


urlpatterns = [
    path('sheet/', views.SheetView.as_view()),
    path('sheet-list/', views.SheetListView.as_view()),
    path('sheet/<int:pk>', views.SheetDetailView.as_view()),
]