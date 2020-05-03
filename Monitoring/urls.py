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
from planning_approvals.views import SiteCreate, SiteUpdate, SiteDelete, PlanningAppUpdate, PlanningAppDelete, PlotCreate, NoteCreate, PlanningAppCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('monitoring/', include('planning_approvals.urls')),
    path('monitoring/accounts/', include('django.contrib.auth.urls')),
    path('monitoring/site/add/', SiteCreate.as_view(), name='site_create'),
    path('monitoring/site/<int:pk>/edit/', SiteUpdate.as_view(), name='site_update'),
    path('monitoring/site/<int:pk>/delete/', SiteDelete.as_view(), name='site_delete'),
    path('monitoring/planningapp/add/', PlanningAppCreate.as_view(), name='planningapp_create'),
    path('monitoring/planningapp/<int:pk>/edit/', PlanningAppUpdate.as_view(), name='planningapp_update'),
    path('monitoring/planningapp/<int:pk>/delete/', PlanningAppDelete.as_view(), name='planningapp_delete'),
    path('monitoring/planningapp/<int:pk>/add-plots/', PlotCreate.as_view(), name='plot_create'),
    path('monitoring/planningapp/<int:pk>/add-notes/', NoteCreate.as_view(), name='note_create'),
]
