from django.db import models
from django.db.models import Count, Q
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class Parish(models.Model):
    parish = models.CharField(max_length=20, blank=True, null=True)
    settlement = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
         """String for representing the model object (in Admin site etc.)."""
         return self.parish
        
    class Meta:
        verbose_name_plural='Parishes'
  

class Site(models.Model):
    """Model for site which serves groups planning apps and allocations"""

    # Fields
    site_ref = models.CharField(max_length=20, help_text='Reference for site')
    site_name = models.CharField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)    

    # Metadata
    class Meta: 
        ordering = ['site_ref']

    # Methods
#    def get_absolute_url(self):
#        """Returns the url to access a particular instance of MyModelName."""
#        return reverse('model-detail-view', args=[str(self.site_ref)])

    def get_absolute_url(self):
        return reverse('site-detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the model object (in Admin site etc.)."""
        return self.site_ref

    
    
class PlanningApp(models.Model):
    app_ref = models.CharField(max_length=20)
    policy = models.CharField(max_length=20, blank=True, null=True)
    superseded_by_app = models.CharField(max_length=20, blank=True, null=True)
    superseded_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    address = models.TextField()
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE, blank=True, null=True)
    proposal = models.TextField()
    
    APP_TYPE_CHOICES = (
        ('a', 'Allocation'),
        ('f', 'Full Planning'),
        ('o', 'Outline'),
        ('pn', 'Prior Notification'),
        ('pip', 'Permission in Priciple'),
        ('rm', 'Reserved Matters'),
        )
    
    app_type = models.CharField(
        max_length=5,
        choices=APP_TYPE_CHOICES,
        blank=True,
        null=True,
        help_text='Permission type',
    )
    
    decision_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    appeal_decision_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    committee_decision_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    lapse_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    
    DEV_TYPE_CHOICES = (
        ('new', 'New Building(s)'),
        ('cou', 'Change of Use'),
        ('rebld', 'Rebuild Applications'),
        ('conv', 'Conversion of a dwellings'),
        ('dem', 'Demolition of floorspace'),
        )
    
    dev_type = models.CharField(
        max_length=5,
        choices=DEV_TYPE_CHOICES,
        blank=True,
        null=True, 
        help_text='Development type',
    )
    
        
    DEV_CLASS_CHOICES = (
        ('inf', 'Infill 1-2 dwellings'),
        ('grp', 'Group 3-8 dwellings'),
        ('est', 'Estate 9+ dwellings'),
        ('cou', 'Residential Change of Use'),
        ('con', 'Residential conversion'),
        ('dem', 'Demolition of a dwelling'),
        ('prk', 'Park Homes development'),
        ('rep', 'Replacement dwelling'),        
        )
    
    dev_class = models.CharField(
        max_length=5,
        choices=DEV_CLASS_CHOICES,
        blank=True,
        null=True, 
        help_text='Development class',
    )
    
    PDL_CHOICES = (
        ('g', 'Greenfield'),
        ('b', 'Brownfield'),
        ('m', 'Mix of Greenfield and Brownfield'),
        )
    
    pdl = models.CharField(
        max_length=1,
        choices=PDL_CHOICES,
        blank=True,
        null=True, 
        help_text='Greenfield / Brownfield land',
    )
    
    site_capacity = models.IntegerField(default=0, blank=True, null=True, help_text='Total no. of dwellings permitted')
    units_lost = models.IntegerField(default=0, blank=True, null=True, help_text='No. of dwellings lost through development of site')
    
    lapsed = models.BooleanField(default=False, help_text='Where permission not implemented before lapse date, manually set application to \'lapsed\' status')
    not_applicable = models.BooleanField(default=False, help_text='Omit site from monitoring data, without deleting record')
    
    current_status = models.CharField(max_length=30, default="Extant", blank=True, null=True, help_text='(Auto) Defines current status of planning permission')
    
    #trajectory
    year_01 = models.IntegerField(default=0, blank=True, null=True)
    year_02 = models.IntegerField(default=0, blank=True, null=True)
    year_03 = models.IntegerField(default=0, blank=True, null=True)
    year_04 = models.IntegerField(default=0, blank=True, null=True)
    year_05 = models.IntegerField(default=0, blank=True, null=True)
    year_06 = models.IntegerField(default=0, blank=True, null=True)
    year_07 = models.IntegerField(default=0, blank=True, null=True)
    year_08 = models.IntegerField(default=0, blank=True, null=True)
    year_09 = models.IntegerField(default=0, blank=True, null=True)
    year_10 = models.IntegerField(default=0, blank=True, null=True)
    year_11 = models.IntegerField(default=0, blank=True, null=True)
    year_12 = models.IntegerField(default=0, blank=True, null=True)
    year_13 = models.IntegerField(default=0, blank=True, null=True)
    year_14 = models.IntegerField(default=0, blank=True, null=True)
    year_15 = models.IntegerField(default=0, blank=True, null=True)
    year_16 = models.IntegerField(default=0, blank=True, null=True)
    year_17 = models.IntegerField(default=0, blank=True, null=True)
    year_18 = models.IntegerField(default=0, blank=True, null=True)
    year_19 = models.IntegerField(default=0, blank=True, null=True)
    year_20 = models.IntegerField(default=0, blank=True, null=True)
    
    traj_comments = models.TextField(blank=True, null=True)
    traj_internal_notes = models.TextField(blank=True, null=True)
    
    
    DELIVERABLE_CHOICES = (
        ('A', 'a) Site is not major development'),
        ('B', 'b) Site with detailed planning permission'),
        ('C', 'c) Site with outline planning permission with clear evidence that housing completions will begin on site within five years'),
        ('D', 'd) Site with permission in principle with clear evidence that housing completions will begin on site within five years'),
        ('E', 'e) Site allocated within the development plan with clear evidence that housing completions will begin on site within five years'),
        ('F', 'f) Site identified on a brownfield register with clear evidence that housing completions will begin on site within five years'),
        ('G', 'g) Site without consent but with clear evidence that housing completions will begin on site within five years'),
        ('H', 'h) Site is not considered deliverable within five years or there is insufficient evidence site will be delivered within five years'),
        )
    
    deliverable = models.CharField(
        max_length=1,
        choices=DELIVERABLE_CHOICES,
        blank=True,
        null=True, 
        help_text='How permission meets deliverable definition in national policy',
    )
    
    # additional applications and planning history
    additional_app = models.TextField(blank=True, null=True, help_text='Relevant details of additional applications (e.g. new applications pending determination)')
    planning_history = models.TextField(blank=True, null=True, help_text='Details of previous applications on site')
    application_docs_url = models.URLField(max_length=255, blank=True, null=True, help_text='Link to online planning application documents')
    
    # map / location info
    site_plan_url = models.URLField(max_length=255, blank=True, null=True, help_text='Link to site plan')
    easting = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    northing = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    site_area = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)
    
 
    # log of created / updated date
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    

    # @property calcs
    @property
    def net_gain(self):
        return self.site_capacity - self.units_lost
    
    @property
    def five_year_total(self):
        return (
            self.year_01 +
            self.year_02 +
            self.year_03 +
            self.year_04 +
            self.year_05
            )
    
    @property
    def trajectory_total(self):
        return (
            self.year_01 +
            self.year_02 +
            self.year_03 +
            self.year_04 +
            self.year_05 +
            self.year_06 +
            self.year_07 +
            self.year_08 +
            self.year_09 +
            self.year_10 +
            self.year_11 +
            self.year_12 +
            self.year_13 +
            self.year_14 +
            self.year_15 +
            self.year_16 +
            self.year_17 +
            self.year_18 +
            self.year_19 +
            self.year_20
            )
    
    @property
    def plots_not_started(self):
        return Plot.objects.filter(planning_app=self.id).filter(commenced_date=None).filter(completed_date=None).count()
    
    
    @property
    def plots_commenced(self):
        return Plot.objects.filter(planning_app=self.id).filter(commenced_date__gte=datetime.date(1900, 1, 1)).exclude(completed_date__gte=datetime.date(1900, 1, 1)).count()
    
    @property
    def plots_completed(self):
        return Plot.objects.filter(planning_app=self.id).filter(completed_date__gte=datetime.date(1900, 1, 1)).exclude(plot_dev="dem").count()

    @property
    def plots_demolished(self):
        return Plot.objects.filter(planning_app=self.id).filter(completed_date__gte=datetime.date(1900, 1, 1)).filter(plot_dev="dem").count()

    @property
    def total_plots(self):
        return Plot.objects.filter(planning_app=self.id).count()
    
    @property
    def net_commitment(self):
        return self.site_capacity - self.plots_completed
    
    @property
    def density(self):
        if self.site_area >0:
            return self.site_capacity / self.site_area
        else:
            return None

    def save(self):
        if self.superseded_by_app not in [None, ""]:
            self.current_status = "Superseded"
            
        elif self.lapsed == True:
            self.current_status = "Lapsed"
            
        elif self.not_applicable == True:
            self.current_status = "Not applicable"
            
        elif self.plots_completed == self.site_capacity:
            self.current_status = "Completed"
            
        else:
            self.current_status = "Extant"
            
        super().save()
        
    def get_absolute_url(self):
        return reverse('planningapp-detail', args=[str(self.id)])
        
    def __str__(self):
        """String for representing the model object (in Admin site etc.)."""
        return self.app_ref
       
    class Meta:
        ordering = ['app_ref']
    
class Note(models.Model):
    planning_app = models.ForeignKey(PlanningApp, on_delete=models.CASCADE)
    body = models.TextField(help_text='Add a note')    
    created_on = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """String for representing the model object (in Admin site etc.)."""
        return "Added " + (str(self.created_on))[:10] + " by " + str(self.author)

class Plot(models.Model):
    address = models.CharField(max_length=60, blank=True, null=True)
    planning_app = models.ForeignKey(PlanningApp, on_delete=models.CASCADE)
    plot_no = models.CharField(max_length=20, blank=True, null=True)
    bc_ref = models.CharField(max_length=20, blank=True, null=True)
    beds = models.IntegerField(blank=True, null=True)
    
    TENURE_CHOICES = (
        ('m', 'Market'),
        ('a', 'Affordable'),
        ('i', 'Intermediate'),
        ('s', 'Starter Homes')
        )
    
    tenure = models.CharField(
        max_length=1,
        choices=TENURE_CHOICES,
        blank=True,
        null=True, 
        help_text='Select tenure',
    )
    
    PLOT_TYPE_CHOICES = (
        ('bs', 'Bedsits / studios'),
        ('cf', 'Cluster flats'),
        ('fm', 'Flats / maisonettes'),
        ('hb', 'Houses / bungalows'),
        ('lw', 'Live-work units'),
        ('ph', 'Park homes'),
        ('sh', 'Sheltered housing'),
        ('sb', 'Self-build plots'),
        ('un', 'Unknown'),
        )
    
    plot_type = models.CharField(
        max_length=2,
        choices=PLOT_TYPE_CHOICES,
        blank=True,
        null=True, 
        help_text='Select plot type',
    )
    
    
    PLOT_DEV_CHOICES = (
        ('cou', 'Change of Use'),
        ('con', 'Conversion of a dwelling'),
        ('dem', 'Demolition'),
        ('new', 'New building'),
        ('reb', 'Rebuild application'),
        )
    
    plot_dev = models.CharField(
        max_length=3,
        choices=PLOT_DEV_CHOICES,
        blank=True,
        null=True, 
        help_text='Select development type',
    )
    
    commenced_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    completed_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    superseded_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    superseded_by_app = models.CharField(max_length=20, blank=True, null=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String for representing the model object (in Admin site etc.)."""
        return self.plot_no
    


    