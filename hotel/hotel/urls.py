"""hotel URL Configuration

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
    path('module-bills/', include('module_bills.urls')),
    path('module-staff/', include('module_staff.urls')),
    path('module-guests/', include('module_guests.urls')),
    path('module-payments/', include('module_payments.urls')),
    path('module-services/', include('module_services.urls')),
    path('module-checkin/', include('module_checkin.urls')),
    path('module-bookings/', include('module_bookings.urls')),
    path('module-rooms/', include('module_rooms.urls')),
    path('module-assets/', include('module_assets.urls')),
    path('module-housekeeping/', include('module_housekeeping.urls')),
    path('module-portal/', include('module_portal.urls')),
    path('module-settings/', include('module_settings.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
