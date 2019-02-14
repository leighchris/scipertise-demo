from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from taggit.forms import *


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'expert', 'wants_expert', 'needs_help_with', )
        help_texts = {
            'expert': 'Check the box if you would like to be an expert or mentor. This is required to create an expert profile.',
            'wants_expert': 'Check the box if you are interested in finding expertise. Otherwise leave blank.',
            'needs_help_with': 'This information is confidential and will not be published anywhere.',
           
        }
        labels = {
            'expert': 'Would you like to provide expertise?',
            'wants_expert': 'Would you like to get help with your research or learn a new technique?',
            'needs_help_with': 'If you answered yes, what are some skills or topics you would like to get help with or learn better (be specific)?',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'needs_help_with': forms.Textarea(attrs={'class': 'form-control'}),
            
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].required = True
        
        
class EditProfile(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields =('username','position', 'website', 'bio', 'skills', 'software_hardware', 'software_hardware_intermediate', 'skill_area1_title', 'skill_area1', 'skill_area2_title', 'skill_area2', 'skill_area3_title', 'skill_area3', 'skill_area4_title', 'skill_area4', 'skill_area5_title', 'skill_area5', 'gives_tutorials', 'tutorial_area', )
        help_texts = {
            'username': "If you'd like to change your username, enter a new username above",
            'position': "Example: Postdoctoral Fellow in Neuroscience at McGill University",
            
            'skills': "Example: fMRI, cognitive neuroscience, EEG, memory, functional connectivity",
            'bio': "Describe your general experience/expertise in your field in 2-3 sentences.",
            
            'software_hardware': "Enter the names of relevant equipment, hardware, or software you are 'expert level' at, separated by                  commas",
            'software_hardware_intermediate': "Enter the names of relevant equipment, hardware, or software you are 'intermediate                        level' at, separated by commas",
            'skill_area1_title': "Example: I'm use pain psychophysical measures and quantitative sensory testing with patients in a                     clinical setting.",
            'skill_area1': "Example: Completed several investigations using a pain psychophysics protocol involving thermal, mechanical                 and electrical stimulation. I often host workshops and teach courses on this topic.",
            'skill_area2_title': "Example: I'm an experienced researcher on the topics of chronic pain and peripheral neuropathy                       characteristics and symptoms.",
            'skill_area2': "Example: Recently characterized pain-related symptoms and disease-related factors in different chronic pain                 populations - several first and senior author publications on this topic.",
            'skill_area3_title': "Example: I'm experience with task-based fMRI experiment design and fMRI analysis using FSL software                   and psychophysics toolbox (MATLAB).",
            'skill_area3': "Example: I have designed several tasks for the fMRI environment to measure pain perception, and have                        published two papers in which I completed task-based and connectivity analyses.",
            'skill_area4_title': "Example: Studiyng sex differences and the brain",
            'skill_area4': "I'm currently investigating sex differences in resting state brain activity in a human chronic pain                         population", 
            
        }
        
        labels = {
             'position': "Enter your current position and location (institution or company)",
             'website': "Please add the url for your Google Scholar profile below (optional)",
             
             'skills': "Enter up to 6 keywords describing your skills to help people find you, separated by commas. Do not               include slashes in the skill tag name",
             'bio': "Provide a short bio",
             'software_hardware': "Equipment or software you are 'expert level' at:",
             'software_hardware_intermediate': "Equipment or software you are 'intermediate level' at:", 
             'skill_area1_title': "Describe your first skill in 1-2 sentences",
             'skill_area1': "Give examples of experience(s) that allowed you to gain or demonstrate this skill",
             'skill_area2_title': 'Describe your second skill in 1-2 sentences',
             'skill_area2': "Give examples of experience(s) that allowed you to gain or demonstrate this skill",
             'skill_area3_title': 'Describe your third skill in 1-2 sentences (optional)',
             'skill_area3': "Give examples of experience(s) that allowed you to gain or demonstrate this skill",
             'skill_area4_title': 'Describe your fourth skill in 1-2 sentences (optional)',
             'skill_area4': "Give examples of experience(s) that allowed you to gain or demonstrate this skill",
             'skill_area5_title': 'Describe your fifth skill in 1-2 sentences (optional)',
             'skill_area5': "Give examples of experience(s) that allowed you to gain or demonstrate this skill",
             'gives_tutorials': "Check this box if you are interested in leading video chat tutorials or small group lessons in your                      area of expertise",
             'tutorial_area': "If you checked the box above to lead tutorials/group lessons, please give examples of topics/technical                    skills you would be willing to teach",
                
         }
        widgets = {
                'bio': forms.Textarea(),
                'skill_area1': forms.Textarea(),
                'skill_area2': forms.Textarea(),
                'skill_area3': forms.Textarea(),
                'skill_area4': forms.Textarea(),
                'skill_area5': forms.Textarea(),
                'tutorial_area': forms.Textarea(),

            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['position'].required = True
        self.fields['website'].required = False
        self.fields['bio'].required = False
        self.fields['skills'].required = False
        self.fields['software_hardware'].required  = False
        self.fields['software_hardware_intermediate'].required  = False
        self.fields['skill_area1_title'].required =False
        self.fields['skill_area1'].required =False
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
        
        
        
       
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        position = cleaned_data.get('position')
        website = cleaned_data.get('website')
        bio = cleaned_data.get('bio')
        skills = cleaned_data.get('skills')
        software_hardware = cleaned_data.get('software_hardware')
        software_hardware_intermediate = cleaned_data.get('software_hardware_intermediate')
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
        
        
class EditProfileDetail(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields =('rate', 'availability', 'gives_tutorials', 'tutorial_area', 'profile_under_review', )
        help_texts = {
            'availability': "Example: Mondays from 6-8pm EST' or 'Sunday evenings and weekdays from 8-10am EST. Please include your                     timezone.",
            'rate': "Please select your hourly rate in CAD dollars (e.g. $50/hour). Scipertise will deduct a platform fee of 15% for                    all transactions. Please set your hourly rate accordingly.",
           
           
        }
        
        labels = {
             'availability': "What times are you generally free during the week?",
             'rate': "Hourly rate (CAD)",

             
             'gives_tutorials': "Check this box if you are interested in leading video chat tutorials or small group lessons in your                      area of expertise",
             'tutorial_area': "If you checked the box above to lead tutorials/group lessons, please give examples of topics/technical                    skills you would be willing to teach",
             'profile_under_review': 'Check this box once your profile is complete. Once you submit your profile, we will review it. If                     you are approved as an expert/ mentor we will notify you within 48 hours of submission.',
                
         }
        widgets = {
                
                'tutorial_area': forms.Textarea(),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'].required = False
        self.fields['availability'].required = False
        self.fields['gives_tutorials'].required = False
        self.fields['tutorial_area'].required =False
        self.fields['profile_under_review'].required =False 
   
       
    def clean(self):
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate')
        availability = cleaned_data.get('availability')
        gives_tutorials = cleaned_data.get('gives_tutorials')
        tutorial_area = cleaned_data.get('tutorial_area')
        profile_under_review = cleaned_data.get('profile_under_review')
       
        
        
#class SubmitProfile(forms.ModelForm):
#    class Meta:
#        model = CustomUser
#        fields =('profile_under_review', )
#        labels = {
#
#             'profile_under_review': 'Check this box once your profile is complete. Once you submit your profile, we will review it. If                     you are approved as an expert/ mentor we will notify you within 48 hours of submission.'
#                
#         }
#        
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['profile_under_review'].required =False 
#       
#    def clean(self):
#        cleaned_data = super().clean()
#        profile_under_review = cleaned_data.get('profile_under_review')
        

        
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
        
        

        
    

    
    
    
