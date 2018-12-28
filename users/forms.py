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
        help_text="Please enter your job title and Institution or Company you work for"
    )
    availability = forms.CharField(
        help_text="Please state the time slots your are available during the week (e.g. Mondays between 6-8pm)"
    )
    rate = forms.CharField(
        help_text="Please select your hourly rate in CAD dollars (e.g. $50/ per hour)"
    )
    bio = forms.CharField(widget=forms.Textarea())
    skills = TagField(
        help_text="Please enter a comma separated list of skills"
    )
    software_hardware = forms.CharField(
        help_text="Please enter a comma separated list of software, programming languages, equipment or hardware you have expertise with"
    )
    gives_tutorials = forms.BooleanField(
        help_text="Check the box if you are open to leading group sessions/ tutorials",
        label = "Are you interested in leading group sessions/ tutorials in your area of expertise?"
    )
    tutorial_area = forms.CharField(
        help_text="Please describe the topics which you can host a group session on"
    )

    class Meta:
        model = CustomUser
        fields =('username','position', 'bio', 'skills', 'availability', 'rate', 'software_hardware', 'gives_tutorials', 'tutorial_area',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['position'].widget.attrs['class'] = 'form-control'
        self.fields['availability'].widget.attrs['class'] = 'form-control'
        self.fields['rate'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['skills'].widget.attrs['class'] = 'form-control'
        self.fields['software_hardware'].widget.attrs['class'] = 'form-control'
        self.fields['gives_tutorials'].widget.attrs['class'] = 'form-control'
        self.fields['tutorial_area'].widget.attrs['class'] = 'form-control'
        
       
    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get('username')
        position = cleaned_data.get('position')
        bio = cleaned_data.get('bio')
        availability = cleaned_data.get('availability')
        rate = cleaned_data.get('rate')
        skills = cleaned_data.get('skills')
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
        
        
    

    
    
    
