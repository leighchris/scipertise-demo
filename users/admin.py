from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, EditProfile
from .models import CustomUser

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('position', 'bio',  )}),

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = EditProfile

admin.site.register(CustomUser, CustomUserAdmin)


