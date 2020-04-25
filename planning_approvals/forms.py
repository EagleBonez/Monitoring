from .models import PlanningApp, Site, Plot, Parish
from django.contrib.auth.models import User
from django.forms import ModelForm

class PlanningAppForm(ModelForm):
    class Meta:
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
            
        
