from .models import PlanningApp, Site, Plot, Parish
from django.contrib.auth.models import User
from django.forms import ModelForm

class PlanningAppForm(ModelForm):
    class Meta:
        model = PlanningApp
        fields = [
            'app_ref',
#             'policy',
#             'site',
#             'address',
            ]
            
        
