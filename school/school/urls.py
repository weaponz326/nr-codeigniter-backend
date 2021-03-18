"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    
    path('accounts/', include('accounts.urls')),
    path('module-admin/', include('module_admin.urls')),
    path('module-portal/', include('module_portal.urls')),
    path('module-parents/', include('module_parents.urls')),
    path('module-assessment/', include('module_assessment.urls')),
    path('module-subjects/', include('module_subjects.urls')),
    path('module-attendance/', include('module_attendance.urls')),
    path('module-students/', include('module_students.urls')),
    path('module-reports/', include('module_reports.urls')),
    path('module-terms/', include('module_terms.urls')),
    path('module-staff/', include('module_staff.urls')),
    path('module-classes/', include('module_classes.urls')),
    # path('module-fees/', include('module_fees.urls')),
    path('module-teachers/', include('module_teachers.urls')),
    path('module-settings/', include('module_settings.urls')),
    # path('module-payments/', include('module_payments.urls')),
    path('module-timetables/', include('module_timetables.urls')),
]
