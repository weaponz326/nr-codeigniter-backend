"""production URL Configuration

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
    path('module-stock/', include('module_stock.urls')),
    path('module-equipment/', include('module_equipment.urls')),
    path('module-purchasing/', include('module_purchasing.urls')),
    path('module-orders/', include('module_orders.urls')),
    path('module-manufacturing/', include('module_manufacturing.urls')),
    path('module-contractors/', include('module_contractors.urls')),
    # path('module-projects/', include('module_projects.urls')),
    path('module-workers/', include('module_workers.urls')),
    # path('module-tasks/', include('module_tasks.urls')),
    path('module-products/', include('module_products.urls')),
    # path('module-roster/', include('module_roster.urls')),
    path('module-materials/', include('module_materials.urls')),
    path('module-portal/', include('module_portal.urls')),
    path('module-settings/', include('module_settings.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
