from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from planning_approvals.models import PlanningApp, Site, Plot, Parish, Note
from planning_approvals.forms import PlanningAppForm

from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.forms import modelformset_factory, inlineformset_factory

from planning_approvals.forms import PlanningAppForm

#Adding new, blank records

class PlanningAppCreate(CreateView):
     template_name = 'planning_approvals/add_planningapp.html'
     model = PlanningApp
     fields = '__all__'
     success_url = reverse_lazy('plot_create') 

class PlotCreate(TemplateView):
    template_name = 'planning_approvals/add_plot.html'
    PlotFormSet = inlineformset_factory(PlanningApp, Plot, fields='__all__')
    
    def get(self, request, pk):
        planningapp = PlanningApp.objects.get(id=pk)
        formset = self.PlotFormSet(instance=planningapp)
        context = {'formset': formset}
        return render(request, self.template_name, context)
    
    def post(self, request, pk): 
        planningapp = PlanningApp.objects.get(id=pk)
        formset = self.PlotFormSet(instance=planningapp)
        
        if request.method == 'POST':
            formset = self.PlotFormSet(self.request.POST, instance=planningapp)
            if formset.is_valid():
                formset.save()
                return redirect('planningapp-detail', pk=planningapp.id)
        
        context = {'formset': formset}
        return render(request, self.template_name, context)
    
class NoteCreate(TemplateView):
    template_name = 'planning_approvals/add_note.html'
    NoteFormSet = inlineformset_factory(PlanningApp, Note, fields='__all__', extra=1)
    
    def get(self, request, pk):
        planningapp = PlanningApp.objects.get(id=pk)
        formset = self.NoteFormSet(instance=planningapp)
        context = {'formset': formset}
        return render(request, self.template_name, context)
    
    def post(self, request, pk): 
        planningapp = PlanningApp.objects.get(id=pk)
        formset = self.NoteFormSet(instance=planningapp)
        
        if request.method == 'POST':
            formset = self.NoteFormSet(self.request.POST, instance=planningapp)
            if formset.is_valid():
                formset.save()
                return redirect('planningapp-detail', pk=planningapp.id)
        
        context = {'formset': formset}
        return render(request, self.template_name, context)



#Editing / updating existing records
class PlanningAppUpdate(TemplateView):
    template_name = 'planning_approvals/planningapp_form.html'
    PlotFormSet = inlineformset_factory(PlanningApp, Plot, fields='__all__', extra=1)
    NoteFormSet = inlineformset_factory(PlanningApp, Note, fields='__all__', extra=1)
        
    
    def get(self, request, pk):
        planningapp = PlanningApp.objects.get(id=pk)
        planningapp_form = PlanningAppForm(instance=planningapp)
        plot_formset = self.PlotFormSet(instance=planningapp)
        note_formset = self.NoteFormSet(instance=planningapp)
        context = {
            'planningapp_form': planningapp_form,
            'plot_formset': plot_formset,
            'note_formset': note_formset,
            }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        planningapp = PlanningApp.objects.get(id=pk)
        planningapp_form = PlanningAppForm(request.POST)
        plot_formset = self.PlotFormSet(request.POST, instance=planningapp)
        note_formset = self.NoteFormSet(request.POST, instance=planningapp)
        
        if planningapp_form.is_valid() and note_formset.is_valid() and plot_formset.is_valid():
            planningapp_form.save()
            plot_formset.save()
            note_formset.save()
            
            return redirect('planningapp-detail', pk=planningapp.id)
        
        context = {
            'planningapp_form': planningapp_form,
            'plot_formset': plot_formset,
            'note_formset': note_formset,
            
            }
        return render(request, self.template_name, context)



# form view classes

class SiteCreate(CreateView):
    model = Site
    fields = '__all__'
    
class SiteUpdate(UpdateView):
    model = Site
    fields = '__all__'
    
class SiteDelete(DeleteView):
    model = Site
    success_url = reverse_lazy('sites')


    

# class PlanningAppUpdate(UpdateView):
#     model = PlanningApp
#     fields = '__all__'
#     success_url = reverse_lazy('planningapps')

class PlanningAppDelete(DeleteView):
    model = PlanningApp
    success_url = reverse_lazy('planningapps')

# index

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

# read-only views
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


# drafts

# class PlanningAppCreate(CreateView):
#     model = PlanningApp
#     fields = [
#         'app_ref',
#             'policy',
#             'superseded_by_app',
#             'superseded_date',
#             'site',
#             'address',
#             'parish',
#             'proposal',
#             'app_type',
#             'decision_date',
#             'appeal_decision_date',
#             'committee_decision_date',
#             'lapse_date',
#             'dev_type',
#             'dev_class',
#             'pdl',
#             'site_capacity',
#             'units_lost',
#             'lapsed',
#             'not_applicable',
#             'current_status',
#             'year_01',
#             'year_02',
#             'year_03',
#             'year_04',
#             'year_05',
#             'year_06',
#             'year_07',
#             'year_08',
#             'year_09',
#             'year_10',
#             'year_11',
#             'year_12',
#             'year_13',
#             'year_14',
#             'year_15',
#             'year_16',
#             'year_17',
#             'year_18',
#             'year_19',
#             'year_20',
#             'traj_comments',
#             'traj_internal_notes',
#             'deliverable',
#             'planning_history',
#             'additional_app',
#             'application_docs_url',
#             'site_plan_url',
#             'easting',
#             'northing',
#             'site_area',
#             'author',
#         ]
#     template_name = 'planning_approvals/create_planningapp_detail.html'

# class AddPlanningAppView(FormView):
#     template_name = 'planning_approvals/create_planningapp_detail.html'
#     form_class = PlanningApp
#     success_url = '/monitoring/sites/'
# 
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)
    