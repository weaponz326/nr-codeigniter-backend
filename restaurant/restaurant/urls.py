"""restaurant URL Configuration

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
    path('module-menu/', include('module_menu.urls')),
    path('module-staff/', include('module_staff.urls')),
    path('module-tables/', include('module_tables.urls')),
    path('module-sittings/', include('module_sittings.urls')),
    path('module-orders/', include('module_orders.urls')),
    path('module-deliveries/', include('module_deliveries.urls')),
    path('module-stock/', include('module_stock.urls')),
    path('module-payments/', include('module_payments.urls')),
    path('module-reservations/', include('module_reservations.urls')),
    path('module-customers/', include('module_customers.urls')),
    path('module-bills/', include('module_bills.urls')),
]
