from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, EditProfile, EditProfileDetail
from .models import CustomUser

#
#class SkillsInline(admin.StackedInline):
#    model = CustomUser.skills.through
#    
#class SkillAdmin(admin.ModelAdmin):
#    inlines = [SkillsInline ,]

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('position', 'bio', 'skills', 'image', 'website', 'skill_area1_title', 'skill_area1', 'skill_area2_title', 'skill_area2', 'skill_area3_title', 'skill_area3', 'skill_area4_title', 'skill_area4', 'skill_area5_title', 'skill_area5' ,'software_hardware', 'software_hardware_intermediate', 'availability', 'rate', 'expert', 'gives_tutorials', 'tutorial_area', 'wants_expert', 'needs_help_with', 'profile_under_review', 'profile_approved',)}),

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = EditProfile
    form_two = EditProfileDetail

    
admin.site.register(CustomUser, CustomUserAdmin)

   







