"""association URL Configuration

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
    path('module-portal/', include('module_portal.urls')),
    path('module-settings/', include('module_settings.urls')),
    path('module-accounts/', include('module_accounts.urls')),
    path('module-members/', include('module_members.urls')),
    path('module-committees/', include('module_committees.urls')),
    # path('module-dues/', include('module_dues.urls')),
    path('module-executives/', include('module_executives.urls')),
    path('module-action-plan/', include('module_action_plan.urls')),
    path('module-budget/', include('module_budget.urls')),
    path('module-attendance/', include('module_attendance.urls')),
    path('module-meetings/', include('module_meetings.urls')),
    path('module-groups/', include('module_groups.urls')),
    path('module-year/', include('module_year.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
