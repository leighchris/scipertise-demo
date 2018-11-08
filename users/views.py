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
    
#class EditProfile(generic.CreateView):
#    form_class = CustomUserChangeForm
#    success_url = reverse_lazy('/users/profile')
#    template_name = 'edit_profile.html' 
    
    
class ProfileView(TemplateView):
    template_name = "profile.html"
    
#def EditProfileView(request):
#    form = EditProfile()
#    first_name = ''
#    last_name = ''
#    bio = ''
#    if request.method == 'POST':
#        form = EditProfile(request.POST)
#        if form.is_valid():
#            form.save()
#            first_name = form.cleaned_data['first_name']
#            last_name = form.cleaned_data['last_name']
#            bio = form.cleaned_data['bio']
#            form = EditProfile()
#        return reverse_lazy('profile')
#    return render(request, 'edit_profile.html', {'form': form})

def EditProfileView(request):
    profile_form = EditProfile()
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, instance =request.user)
        if profile_form.is_valid():
            profile_form.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        profile_form = EditProfile(instance = request.user)
        return render(request, 'edit_profile.html', {'form': form})
    

    

