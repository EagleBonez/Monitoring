from .models import PlanningApp, Site, Plot, Parish, Note
from django.contrib.auth.models import User
from django import forms
from .widgets import FengyuanChenDatePickerInput
from django.conf import settings



class PlanningAppForm(forms.ModelForm):
    class Meta:
        model = PlanningApp
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'cols': 30, 'rows': 3}),
            'proposal': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
            'decision_date': FengyuanChenDatePickerInput(attrs={'autocomplete': 'off'}),
            'appeal_decision_date': FengyuanChenDatePickerInput(attrs={'autocomplete': 'off'}),
            'committee_decision_date': FengyuanChenDatePickerInput(attrs={'autocomplete': 'off'}),
            'lapse_date': FengyuanChenDatePickerInput(attrs={'autocomplete': 'off'}),
            'superseded_date': FengyuanChenDatePickerInput(attrs={'autocomplete': 'off'}),
            'site_capacity': forms.NumberInput(attrs={'class':'form-number'}),
            'units_lost': forms.NumberInput(attrs={'class':'form-number'}),
            }
        
    def __init__(self, *args, **kwargs):
        super(PlanningAppForm, self).__init__(*args, **kwargs)
        self.fields['decision_date'].input_formats=(settings.DATE_INPUT_FORMATS)
        self.fields['appeal_decision_date'].input_formats=(settings.DATE_INPUT_FORMATS)
        self.fields['committee_decision_date'].input_formats=(settings.DATE_INPUT_FORMATS)
        self.fields['lapse_date'].input_formats=(settings.DATE_INPUT_FORMATS)
        self.fields['superseded_date'].input_formats=(settings.DATE_INPUT_FORMATS)
# class PlotForm(forms.ModelForm):
#     class Meta:
#         model = Plot
#         fields = '__all__'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'




# class PlanningAppForm(forms.Form):
#     class Meta:
#         template_name = 'planning_approvals/create_planningapp_detail.html'
#         model = PlanningApp
#         fields = [
#             'app_ref',
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
#             
#             
#             ]
            
        
