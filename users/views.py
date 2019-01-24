from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView, DetailView, FormView, ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, EditProfile, EditProfileDetail, EditProfileImage
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser


class SkillView(ListView):
    model = CustomUser
    template_name = 'users/skills.html'
    queryset = CustomUser.objects.all()
    
    def get_queryset(self):
        queryset = CustomUser.objects.filter(skills__name = self.kwargs['slug'])
        return queryset
    

class BrowseView(ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter(expert = True)

    
#    def get_queryset(self):
#        experts = CustomUser.objects.filter(expert = True)
#        return experts



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
#    
#class LoginView(FormView):
#    form_class = LoginForm
#    template_name = "login.html"

def view_profile(request, pk=None):
    if pk:
        user = CustomUser.objects.get(pk=pk)
    else:
        user = request.user
    bookings = user.bookings.all()
    tutorials = bookings.filter(is_tutorial=True)
    args = {'user': user,
            'bookings': bookings,
            'tutorials': tutorials,
           }
    return render(request, 'profile.html', args)

@login_required
def EditProfileView(request):
    form = EditProfile()
    form_two =EditProfileDetail()
    if request.method == 'POST':
        form = EditProfile(request.POST, instance =request.user)
        form_two = EditProfileDetail(request.POST, instance =request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('edit_profile'))
        if form_two.is_valid():
            form_two.save()
        return HttpResponseRedirect(reverse('profile'))

    else:
        form = EditProfile(instance = request.user)
        form_two = EditProfileDetail(instance = request.user)
       
        return render(request, 'edit_profile.html', {
            'form': form,
            'form_two': form_two,
    
        })
    

#def EditProfileFormsView(MultiFormsView):
#    template_name = "edit_profile.html"
#    form_classes = {'form': EditProfile,
#                    'second_form': EditProfileDetail,
#                    }
#
#    success_urls = {
#        'form': reverse_lazy('edit_profile'),
#        'second_form': reverse_lazy('profile'),
#    }
    
def EditProfileImageView(request):
    form = EditProfileImage()
    if request.method == 'POST':
        form = EditProfileImage(request.POST, request.FILES, instance =request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditProfileImage(instance = request.user)
        return render(request, 'edit_profile_image.html', {'form': form})
    
#def EditProfileImageView(FormView):
#    template_name='edit_profile_image.html'
#    form_class= EditProfileImage
#    success_url = reverse_lazy('profile')
#    
#    def form_valid(self, form):
#        return HttpResponse('form valid')
    
#def change_password(request):
#    
#    if request.method == "POST":
#        form = PasswordChangeForm(request.POST, user=request.user)
#      
#        if form.is_valid():
#            form.save()
#        return HttpResponseRedirect(reverse('profile'))
#    else:
#        form = PasswordChangeForm(user = request.user)
#        return render(request, 'change_password.html', {'form': form})
#    


