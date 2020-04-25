from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from planning_approvals.models import PlanningApp, Site, Plot, Parish
from planning_approvals.forms import PlanningAppForm

from django.views.generic.edit import CreateView, DeleteView, UpdateView

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


# form view classes

class PlanningAppCreate(CreateView):
    model = PlanningApp
    fields = [
        'app_ref',
            'policy',
            'superseded_by_app',
            'superseded_date',
            'site',
            'address',
            'parish',
            'proposal',
            'app_type',
            'decision_date',
            'appeal_decision_date',
            'committee_decision_date',
            'lapse_date',
            'dev_type',
            'dev_class',
            'pdl',
            'site_capacity',
            'units_lost',
            'lapsed',
            'not_applicable',
            'current_status',
            'year_01',
            'year_02',
            'year_03',
            'year_04',
            'year_05',
            'year_06',
            'year_07',
            'year_08',
            'year_09',
            'year_10',
            'year_11',
            'year_12',
            'year_13',
            'year_14',
            'year_15',
            'year_16',
            'year_17',
            'year_18',
            'year_19',
            'year_20',
            'traj_comments',
            'traj_internal_notes',
            'deliverable',
            'planning_history',
            'additional_app',
            'application_docs_url',
            'site_plan_url',
            'easting',
            'northing',
            'site_area',
            'author',
        ]
    template_name = 'planning_approvals/create_planningapp_detail.html'
    