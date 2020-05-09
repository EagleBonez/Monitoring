from django.urls import path
from . import views
from planning_approvals.views import SiteCreate, SiteUpdate, SiteDelete, PlanningAppUpdate, PlanningAppDelete, PlotCreate, NoteCreate, PlanningAppCreate


urlpatterns = [
    path('', views.index, name='index'),
    path('sites/', views.SiteListView.as_view(), name='sites'),
    path('site/<int:pk>', views.SiteDetailView.as_view(), name='site-detail'),
    path('planningapps/', views.Planning_AppListView.as_view(), name='planningapps'),
    path('planningapp/<int:pk>', views.Planning_AppDetailView.as_view(), name='planningapp-detail'),
    path('trajectory/', views.TrajectoryListView.as_view(), name='trajectory'),
    path('site/add/', SiteCreate.as_view(), name='site_create'),
    path('site/<int:pk>/edit/', SiteUpdate.as_view(), name='site_update'),
    path('site/<int:pk>/delete/', SiteDelete.as_view(), name='site_delete'),
    path('planningapp/add/', PlanningAppCreate.as_view(), name='planningapp_create'),
    path('planningapp/<int:pk>/edit/', PlanningAppUpdate.as_view(), name='planningapp_update'),
    path('planningapp/<int:pk>/delete/', PlanningAppDelete.as_view(), name='planningapp_delete'),
    path('planningapp/<int:pk>/addplots/', PlotCreate.as_view(), name='plot_create'),
    path('planningapp/<int:pk>/add-notes/', NoteCreate.as_view(), name='note_create'),
]