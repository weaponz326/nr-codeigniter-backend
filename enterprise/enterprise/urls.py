"""enterprise URL Configuration

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
    path('module-accounts/', include('module_accounts.urls')),
    path('module-payroll/', include('module_payroll.urls')),
    path('module-attendance/', include('module_attendance.urls')),
    path('module-assets/', include('module_assets.urls')),
    path('module-leave/', include('module_leave.urls')),
    path('module-budget/', include('module_budget.urls')),
    path('module-procurement/', include('module_procurement.urls')),
    path('module-letters/', include('module_letters.urls')),
    path('module-appraisal/', include('module_appraisal.urls')),
    path('module-files/', include('module_files.urls')),
    path('module-employees/', include('module_employees.urls')),
    path('module-ledger/', include('module_ledger.urls')),
    path('module-reception/', include('module_reception.urls')),
    path('module-portal/', include('module_portal.urls')),
    path('module-settings/', include('module_settings.urls')),
]
