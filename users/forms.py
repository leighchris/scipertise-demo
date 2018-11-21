from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Skill
from taggit.forms import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email' ,)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
        
class EditProfile(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    position =forms.CharField(help_text="Please enter your job title and Institution/ Company you work for")
    bio = forms.CharField(widget=forms.Textarea())
    skills = TagField(help_text="Please enter a comma separated list of skills")

    class Meta:
        model = CustomUser
        fields =('first_name', 'last_name', 'position', 'bio', 'skills' ,)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['position'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['skills'].widget.attrs['class'] = 'form-control'
        
       
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        position = cleaned_data.get('position')
        bio = cleaned_data.get('bio')
        skills = cleaned_data.get('skills')
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password =forms.CharField(widget =forms.PasswordInput(attrs={'class':'form-control'}))
    

    
    
    
