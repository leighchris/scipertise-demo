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
        help_text="Please enter a username if you would like to change your current username"
    )
    position =forms.CharField(
        label="What is your current job title/ position?",
        help_text="Please enter your job title and Institution or Company you work for (e.g. Postdoctoral Fellow at McGill University)"
    )
    availability = forms.CharField(
        label="What times are you generally available during the week?",
        help_text="Please state the time slots your are available during the week (e.g. Mondays between 6-8pm)"
    )
    rate = forms.CharField(
        
        help_text="Please select your hourly rate in CAD dollars (e.g. $50/ per hour)"
    )
    skills = TagField(
        label="Please list 3-6 keywords for your skills/ expertise",
        help_text="Please enter a comma separated list of skills (e.g. fMRI, cognitive neuroscience, EEG, memory)"
    )
    bio = forms.CharField(widget=forms.Textarea(),
        label="What is your primary area of expertise?",
        help_text="In 2-3 sentences, describe your general experience and expertise in your field"
    )
    skill_area1_title =forms.CharField(
        label="What is the title of your top skill area?",
    )
    skill_area1 =forms.CharField(widget=forms.Textarea(),
        label="Describe your skill area/ experience in 1-3 sentences",
    )
    
    skill_area2_title =forms.CharField(
        label="What is the title of your second skill area (Optional)?",
    )
    skill_area2 =forms.CharField(widget=forms.Textarea(),
        label="Describe your skill area/ experience in 1-3 sentences",
    )
    
    skill_area3_title =forms.CharField(
        label="What is the title of your third skill area (Optional)?",
    )
    skill_area3 =forms.CharField(widget=forms.Textarea(),
        label="Describe your skill area/ experience in 1-3 sentences",
    )
    
    skill_area4_title =forms.CharField(
        label="What is the title of your fourth skill area (Optional)?",
    )
    skill_area4 =forms.CharField(widget=forms.Textarea(),
        label="Describe your skill area/ experience in 1-3 sentences",
    )
    
    skill_area5_title =forms.CharField(
        label="What is the title of your fifth skill area (Optional)?",
    )
    skill_area5 =forms.CharField(widget=forms.Textarea(),
        label="Describe your skill area/ experience in 1-3 sentences",
    )
 
    software_hardware = forms.CharField(
        label="What software, equipment or techniques do you have expertise with",
        help_text="Please enter a comma separated list of software, programming languages, equipment or hardware you have expertise with"
    )
    gives_tutorials = forms.BooleanField(
        help_text="Check the box if you are open to leading group sessions/ tutorials",
        label = "Are you interested in leading group sessions/ tutorials in your area of expertise?"
    )
    tutorial_area = forms.CharField(
        label = "If you answered yes to leading group sessions, what specific topics would you be able to teach?",
        help_text="Please describe in 1-2 sentences the topics/ technical skills which you can host a group session on"
    )

    class Meta:
        model = CustomUser
        fields =('username','position', 'bio', 'skills', 'skill_area1_title', 'skill_area1', 'skill_area2_title', 'skill_area2', 'skill_area3_title', 'skill_area3', 'skill_area4_title', 'skill_area4', 'skill_area5_title', 'skill_area5', 'availability', 'rate', 'software_hardware', 'gives_tutorials', 'tutorial_area',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['position'].required = True
        self.fields['availability'].required = False
        self.fields['rate'].required = False
        self.fields['bio'].required = True
        self.fields['skills'].required =True
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
        self.fields['software_hardware'].required  = False
        self.fields['gives_tutorials'].required = False
        self.fields['tutorial_area'].required =False
        
       
    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get('username')
        position = cleaned_data.get('position')
        bio = cleaned_data.get('bio')
        availability = cleaned_data.get('availability')
        rate = cleaned_data.get('rate')
        skills = cleaned_data.get('skills')
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
        software_hardware = cleaned_data.get('software_hardware')
        gives_tutorials = cleaned_data.get('gives_tutorials')
        tutorial_area = cleaned_data.get('tutorial_area')
        
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
        
        
    

    
    
    
