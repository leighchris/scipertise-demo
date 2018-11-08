from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email' ,)
        
        
class EditProfile(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    position =forms.CharField()
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields =('first_name', 'last_name', 'position', 'bio',)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        position = cleaned_data.get('position')
        bio = cleaned_data.get('bio')
        
#class SkillForm(forms.ModelForm):
#    skill_name = forms.CharField()
#    
#    class Meta:
#        model = Skill
#        fields =('skill_name' ,)
#        
#    def clean(self):
#        cleaned_data = super().clean()
#        skill_name = cleaned_data.get('skill_name')

            
    
