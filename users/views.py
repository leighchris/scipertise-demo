from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .forms import CustomUserCreationForm, EditProfile

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    
class ProfileView(TemplateView):
    template_name = "profile.html"


def EditProfileView(request):
    form = EditProfile()
    if request.method == 'POST':
        form = EditProfile(request.POST, instance =request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditProfile(instance = request.user)
        return render(request, 'edit_profile.html', {'form': form})
    
#def EditSkillView(request):
#    skill_form = SkillForm()
#    if request.method == 'POST':
#        skill_form = SkillForm(request.POST)
#        if skill_form.is_valid():
#            obj = skill_form.save(commit=False)
#            obj.save()
#        # Without this next line the tags won't be saved.
#            skill_form.save_m2m()
#        return HttpResponseRedirect(reverse('profile'))
#    else:
#        skill_form = SkillForm()
#        return render(request, 'edit_skills.html', {'skill_form': skill_form})
#    
#
#    

