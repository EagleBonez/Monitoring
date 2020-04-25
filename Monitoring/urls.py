"""Monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from planning_approvals.views import PlanningAppCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitoring/', include('planning_approvals.urls')),
    path('monitoring/accounts/', include('django.contrib.auth.urls')),
    
    path('monitoring/add/', PlanningAppCreate.as_view(), name='planningapp-add'),
]
