from django.urls import path, include
from . import views


urlpatterns = [
    path('appraisal/', views.AppraisalView.as_view()),
    path('appraisal/<int:pk>', views.AppraisalDetailView.as_view()),
    path('appraisal-form/', views.AppraisalFormView.as_view()),
    path('appraisal-form/<int:pk>', views.AppraisalFormDetailView.as_view()),
    path('refresh-appraisal/', views.RefreshAppraisalView.as_view()),
]