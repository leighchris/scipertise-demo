from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, EditProfile
from .models import CustomUser, Skill, TaggedSkill
admin.site.register(Skill)


admin.site.register(TaggedSkill)

#
#class SkillsInline(admin.StackedInline):
#    model = CustomUser.skills.through
#    
#class SkillAdmin(admin.ModelAdmin):
#    inlines = [SkillsInline ,]

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('position', 'bio', 'skills', 'image', 'skill_area1', 'skill_area2', 'skill_area3', 'skill_area4', 'skill_area5' ,)}),

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = EditProfile
#    inlines = [SkillsInline ,]

    
admin.site.register(CustomUser, CustomUserAdmin)

   







