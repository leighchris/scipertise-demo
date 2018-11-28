from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView, DetailView, FormView
from django.http import HttpResponseRedirect

from .forms import CustomUserCreationForm, EditProfile
from .models import CustomUser

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
    args = {'user': user,
            'bookings': bookings
           }
    return render(request, 'profile.html', args)

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
    


