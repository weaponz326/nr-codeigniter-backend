"""hospital URL Configuration

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
    path('module-settings/', include('module_settings.urls')),
    path('module-patients/', include('module_patients.urls')),
    path('module-appointments/', include('module_appointments.urls')),
    path('module-staff/', include('module_staff.urls')),
    path('module-bills/', include('module_bills.urls')),
    path('module-doctors/', include('module_doctors.urls')),
    path('module-laboratory/', include('module_laboratory.urls')),
    path('module-payments/', include('module_payments.urls')),
    path('module-nurses/', include('module_nurses.urls')),
    path('module-diagnosis/', include('module_diagnosis.urls')),
    path('module-prescriptions/', include('module_prescriptions.urls')),
    path('module-drugs/', include('module_drugs.urls')),
    path('module-admissions/', include('module_admissions.urls')),
    path('module-wards/', include('module_wards.urls')),
    path('module-dispensary/', include('module_dispensary.urls')),
]
