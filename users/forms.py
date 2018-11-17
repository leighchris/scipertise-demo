from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Skill
from taggit.forms import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email' ,)
        
        
class EditProfile(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    position =forms.CharField()
    bio = forms.CharField(widget=forms.Textarea)
    skills = TagField()

    class Meta:
        model = CustomUser
        fields =('first_name', 'last_name', 'position', 'bio', 'skills')

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        position = cleaned_data.get('position')
        bio = cleaned_data.get('bio')
        skills = cleaned_data.get('skills')
        
#class SkillForm(forms.ModelForm):
#    name = forms.CharField()
#    
#    class Meta:
#        model = Skill
#        fields =('name' ,)
#        
#    def clean(self):
#        cleaned_data = super().clean()
#        name = cleaned_data.get('name')

            
    
