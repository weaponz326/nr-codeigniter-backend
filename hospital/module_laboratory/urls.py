from django.urls import path, include
from . import views


urlpatterns = [
    path('lab/', views.LaboratoryView.as_view()),
    path('lab/<int:pk>', views.LaboratoryDetailView.as_view()),
    path('attachment/', views.AttachmentView.as_view()),
    path('attachment/<int:pk>', views.AttachmentDetailView.as_view()),
]