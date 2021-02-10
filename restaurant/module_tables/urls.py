from django.urls import path, include
from . import views


urlpatterns = [
    path('table/', views.TableView.as_view()),
    path('table-list/', views.TableListView.as_view()),
    path('table/<int:pk>', views.TableDetailView.as_view()),
]