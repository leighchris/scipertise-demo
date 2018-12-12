from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Skill
from taggit.forms import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'expert',)
        help_texts = {
            'expert': 'Check the box if you would like to be an expert. Otherwise leave blank.',
        }
        labels = {
            'expert': 'Would you like to provide expertise?',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
        
class EditProfile(forms.ModelForm):
    position =forms.CharField(
        help_text="Please enter your job title and Institution or Company you work for"
    )
    availability = forms.CharField(
        help_text="Please state the time slots your are available during the week (e.g. Mondays and Wednesdays between 6-8pm)"
    )
    rate = forms.CharField(
        help_text="Please select your hourly rate (e.g. $50/ per hour)"
    )
    bio = forms.CharField(widget=forms.Textarea())
    skills = TagField(
        help_text="Please enter a comma separated list of skills"
    )

    class Meta:
        model = CustomUser
        fields =('position', 'bio', 'skills', 'availability', 'rate' ,)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].widget.attrs['class'] = 'form-control'
        self.fields['availability'].widget.attrs['class'] = 'form-control'
        self.fields['rate'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['skills'].widget.attrs['class'] = 'form-control'
        
       
    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get('position')
        bio = cleaned_data.get('bio')
        bio = cleaned_data.get('availability')
        bio = cleaned_data.get('rate')
        skills = cleaned_data.get('skills')
        
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
        
        
    

    
    
    
