from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Site, PlanningApp, Plot, Note, Parish


class ParishAdmin(admin.ModelAdmin):
    list_display = ('parish', 'settlement')
    list_filter = ('parish', 'settlement')
    search_fields = ('parish', 'settlement')


class PlanningAppInline(admin.StackedInline):
    model = PlanningApp
    extra = 0
    fields = [("address", "proposal")]
    

class SiteAdmin(admin.ModelAdmin):
    inlines = [
        PlanningAppInline,
    ]

class NoteInline(admin.StackedInline):
    model = Note
    extra = 1

class PlotInline(admin.StackedInline):
    model = Plot
    extra = 1
    
    fields = [
        ('plot_no', 'bc_ref'),
        ('beds', 'tenure'),
        ('plot_type', 'plot_dev'),
        ('commenced_date', 'completed_date'),
        ('superseded_date', 'superseded_by_app'),
        ]

class PlanningAppAdmin(admin.ModelAdmin):
    list_display = ('app_ref', 'site', 'address', 'parish', 'proposal', 'current_status', 'decision_date', 'appeal_decision_date')
    list_filter = ('app_ref', 'site', 'parish', 'current_status', 'decision_date', 'appeal_decision_date')
    search_fields = ('app_ref', 'site', 'address', 'parish', 'proposal', 'current_status', 'decision_date', 'appeal_decision_date')
    
    fields = [
    
    ('app_ref', 'policy'),
    ('site', 'current_status'),
    ('superseded_by_app', 'superseded_date'),
    ('lapsed', 'not_applicable'),
    'address',
    'parish',
    'proposal',
    'app_type',
    ('decision_date', 'appeal_decision_date'),
    ('committee_decision_date', 'lapse_date'),
    ('dev_type', 'dev_class'),
    ('pdl', 'site_area'),
    ('site_capacity', 'units_lost', 'net_gain'),
    ('plots_commenced', 'plots_completed', 'plots_demolished', 'total_plots', 'net_commitment'),
    ('year_01', 'year_02', 'year_03', 'year_04'),
    ('year_05', 'year_06', 'year_07', 'year_08'),
    ('year_09', 'year_10', 'year_11', 'year_12'),
    ('year_13', 'year_14', 'year_15', 'year_16'),
    ('year_17', 'year_18', 'year_19', 'year_20'),
    ('five_year_total', 'trajectory_total'),
    'traj_comments',
    'traj_internal_notes',
    'deliverable',
    'planning_history',
    'additional_app',
    'application_docs_url',
    'site_plan_url',
    ('easting', 'northing'),
    'author',
    ]
    
    
    
    readonly_fields = [
        'net_gain',
        'five_year_total',
        'trajectory_total',
        'plots_commenced',
        'plots_completed',
        'plots_demolished',
        'total_plots',
        'net_commitment',
        ]
    
    inlines = [
        NoteInline,
        PlotInline,
    ]


admin.site.register(Site, SiteAdmin)
admin.site.register(Parish, ParishAdmin)
#admin.site.register(Note)
admin.site.register(PlanningApp, PlanningAppAdmin)

