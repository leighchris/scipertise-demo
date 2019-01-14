from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from taggit.forms import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'expert', 'gives_tutorials', )
        help_texts = {
            'expert': 'Check the box if you would like to be an expert. Otherwise leave blank.',
            'gives_tutorials': 'Check the box if you are open to leading group sessions/tutorials in your area of expertise.'
            
        }
        labels = {
            'expert': 'Would you like to provide expertise?',
            'gives_tutorials': 'If you answered yes to providing expertise, are you interested in leading group sessions?'
           
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].required = True
        
        
class EditProfile(forms.ModelForm):
    username =forms.CharField(
        help_text="If you'd like to change your username, enter a new username above"
    )
    position =forms.CharField(
        label="Enter your current position and location (institution or company)",
        help_text="Example: Postdoctoral Fellow in Neuroscience at McGill University"
    )
    website = forms.CharField(
        label="Please add the url for your Google Scholar profile (optional)",
    )
    availability = forms.CharField(
        label="What times are you generally free during the week?",
        help_text="Example: Mondays from 6-8pm EST' or 'Sunday evenings and weekdays from 8-10am EST. Please include your timezone."
    )
    rate = forms.CharField(
        
        help_text="Please select your hourly rate in CAD dollars (e.g. $50)",
        label="Hourly rate (CAD)"
    )
    skills = TagField(
        label="Enter 3-6 keywords (maximum of 6) describing your skills to help people find you, separated by commas. Do not include slashes in the skill tag name",
        help_text="Example: fMRI, cognitive neuroscience, EEG, memory, functional connectivity"
    )
    bio = forms.CharField(widget=forms.Textarea(),
        label="What is your primary area of expertise?",
        help_text="Describe your general experience/expertise in your field in 2-3 sentences."
    )
    skill_area1_title =forms.CharField(
        label="Describe your first skill in 1-2 sentences",
        help_text="Example: I'm use pain psychophysical measures and quantitative sensory testing with patients in a clinical setting."
    )
    skill_area1 =forms.CharField(widget=forms.Textarea(),
        label="Give examples of experience(s) that allowed you to gain or demonstrate this skill",
        help_text="Example: Completed several investigations using a pain psychophysics protocol involving thermal, mechanical and electrical stimulation. I often host workshops and teach courses on this topic."
    )
    
    skill_area2_title =forms.CharField(
        label="Describe your second skill in 1-2 sentences",
        help_text="Example: I'm an experienced researcher on the topics of chronic pain and peripheral neuropathy characteristics and symptoms."
    )
    skill_area2 =forms.CharField(widget=forms.Textarea(),
        label="Give examples of experience(s) that allowed you to gain or demonstrate this skill",
        help_text="Example: Recently characterized pain-related symptoms and disease-related factors in different chronic pain populations - several first and senior author publications on this topic."
    )
    
    skill_area3_title =forms.CharField(
        label="Describe your third skill in 1-2 sentences (optional)",
        help_text="Example: I'm experience with task-based fMRI experiment design and fMRI analysis using FSL software and psychophysics toolbox (MATLAB)."
    )
    skill_area3 =forms.CharField(widget=forms.Textarea(),
        label="Give examples of experience(s) that allowed you to gain or demonstrate this skill",
        help_text="Example: I have designed several tasks for the fMRI environment to measure pain perception, and have published two papers in which I completed task-based and connectivity analyses."
    )
    
    skill_area4_title =forms.CharField(
        label="Describe your fourth skill in 1-2 sentences (optional)",
        help_text="Example: Studiyng sex differences and the brain"
    )
    skill_area4 =forms.CharField(widget=forms.Textarea(),
        label="Give examples of experience(s) that allowed you to gain or demonstrate this skill",
        help_text="I'm currently investigating sex differences in resting state brain activity in a human chronic pain population"
    )
    
    skill_area5_title =forms.CharField(
        label="Describe your fifth skill in 1-2 sentences (optional)",
    )
    skill_area5 =forms.CharField(widget=forms.Textarea(),
        label="Give examples of experience(s) that allowed you to gain or demonstrate this skill",
    )
 
    software_hardware = forms.CharField(
        label="Enter the names of relevant equipment, hardware, or software you are 'expert level' at:",
        help_text="Enter the names of relevant equipment, hardware, or software you are 'expert level' at, separated by commas"
    )
    gives_tutorials = forms.BooleanField(
        label = "Check this box if you are interested in leading video chat tutorials or small group lessons in your area of expertise"
    )
    tutorial_area = forms.CharField(
        label = "If you checked the box above to lead tutorials/group lessons, please give examples of topics/technical skills you would be willing to teach",
        
    )

    class Meta:
        model = CustomUser
        fields =('username','position', 'website', 'bio', 'skills', 'software_hardware', 'skill_area1_title', 'skill_area1', 'skill_area2_title', 'skill_area2', 'skill_area3_title', 'skill_area3', 'skill_area4_title', 'skill_area4', 'skill_area5_title', 'skill_area5', 'gives_tutorials', 'tutorial_area', 'rate', 'availability',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['position'].required = True
        self.fields['website'].required = False
        self.fields['bio'].required = True
        self.fields['skills'].required =True
        self.fields['software_hardware'].required  = False
        self.fields['skill_area1_title'].required =True
        self.fields['skill_area1'].required =True
        self.fields['skill_area2_title'].required =False
        self.fields['skill_area2'].required =False
        self.fields['skill_area3_title'].required =False
        self.fields['skill_area3'].required =False
        self.fields['skill_area4_title'].required =False
        self.fields['skill_area4'].required =False
        self.fields['skill_area5_title'].required =False
        self.fields['skill_area5'].required =False
        self.fields['gives_tutorials'].required = False
        self.fields['tutorial_area'].required =False     
        self.fields['rate'].required = False
        self.fields['availability'].required = False
        
        
       
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        position = cleaned_data.get('position')
        website = cleaned_data.get('website')
        bio = cleaned_data.get('bio')
        skills = cleaned_data.get('skills')
        software_hardware = cleaned_data.get('software_hardware')
        skill_area1_title = cleaned_data.get('skill_area1_title')
        skill_area1 = cleaned_data.get('skill_area1')
        skill_area2_title = cleaned_data.get('skill_area2_title')
        skill_area2 = cleaned_data.get('skill_area2')
        skill_area3_title = cleaned_data.get('skill_area3_title')
        skill_area3 = cleaned_data.get('skill_area3')
        skill_area4_title = cleaned_data.get('skill_area4_title')
        skill_area4 = cleaned_data.get('skill_area4')
        skill_area5_title = cleaned_data.get('skill_area5_title')
        skill_area5 = cleaned_data.get('skill_area5')
        gives_tutorials = cleaned_data.get('gives_tutorials')
        tutorial_area = cleaned_data.get('tutorial_area')
        rate = cleaned_data.get('rate')
        availability = cleaned_data.get('availability')
     
        
class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password =forms.CharField()
    
    class Meta:
        model = CustomUser
        fields =('username', 'password',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        
class EditProfileImage(forms.ModelForm):
    image=forms.ImageField()
   
    class Meta:
        model = CustomUser
        fields =('image',)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        
    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get('image')
       
        
    

    
    
    
