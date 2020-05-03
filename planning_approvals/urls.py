from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sites/', views.SiteListView.as_view(), name='sites'),
    path('site/<int:pk>', views.SiteDetailView.as_view(), name='site-detail'),
    path('planningapps/', views.Planning_AppListView.as_view(), name='planningapps'),
    path('planningapp/<int:pk>', views.Planning_AppDetailView.as_view(), name='planningapp-detail'),
    path('trajectory/', views.TrajectoryListView.as_view(), name='trajectory'),
    
]