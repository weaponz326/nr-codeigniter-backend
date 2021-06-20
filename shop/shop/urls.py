"""shop URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    
    path('accounts/', include('accounts.urls')),
    path('module-admin/', include('module_admin.urls')),
    path('module-receivables/', include('module_receivables.urls')),
    path('module-products/', include('module_products.urls')),
    path('module-invoice/', include('module_invoice.urls')),
    path('module-marketting/', include('module_marketting.urls')),
    path('module-payables/', include('module_payables.urls')),
    path('module-sales/', include('module_sales.urls')),
    path('module-customers/', include('module_customers.urls')),
    path('module-payments/', include('module_payments.urls')),
    path('module-orders/', include('module_orders.urls')),
    path('module-inventory/', include('module_inventory.urls')),
    path('module-suppliers/', include('module_suppliers.urls')),
    path('module-staff/', include('module_staff.urls')),
    path('module-cashflow/', include('module_cashflow.urls')),
    path('module-purchasing/', include('module_purchasing.urls')),
    path('module-roster/', include('module_roster.urls')),
    path('module-portal/', include('module_portal.urls')),
    path('module-settings/', include('module_settings.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
