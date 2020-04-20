from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from planning_approvals.models import PlanningApp, Site, Plot, Parish
from planning_approvals.forms import PlanningAppForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_sites = Site.objects.all().count()
    num_planning_apps = PlanningApp.objects.all().count()
    num_plots = Plot.objects.all().count()
    
    # Available books (status = 'a')
    num_extant_apps = PlanningApp.objects.filter(current_status__exact='Extant').count()
    
    # The 'all()' is implied by default.    
    num_parish = Parish.objects.count()
    
    context = {
        'num_sites': num_sites,
        'num_planning_apps': num_planning_apps,
        'num_plots': num_plots,
        'num_extant_apps': num_extant_apps,
        'num_parish': num_parish,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class SiteListView(generic.ListView):
    model = Site
    
class SiteDetailView(generic.DetailView):
    model = Site
    
class Planning_AppListView(generic.ListView):
    model = PlanningApp

class Planning_AppDetailView(generic.DetailView):
    model = PlanningApp


class TrajectoryListView(generic.ListView):
    model = PlanningApp
    template_name = 'planning_approvals/traj_list.html'
    