from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, EditProfile, EditProfileDetail, EditProfileImage
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser
from django.core.mail import send_mail, mail_admins  

from django.template.loader import render_to_string
from django.utils.html import strip_tags


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

    


def login_success(request):
    """
    Redirects users based on whether they are in an expert
    """
#    queryset = CustomUser.objects.filter(wants_expert = True)

    if request.user.wants_expert == True:
        # user needs help
        return HttpResponseRedirect(reverse('booking:help_form'))
    else:
        return  HttpResponseRedirect(reverse('home'))
    
#class HelpView(FormView):
#    form_class = HelpForm
#    success_url = reverse_lazy('home')
#    template_name = 'help_form.html'
#    
#    def form_valid(self, form):
#        # This method is called when valid form data has been POSTed.
#        # It should return an HttpResponse.
#        return super().form_valid(form)



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        user_email = instance.email
        html_message = render_to_string('signup_success_user.html', {'user': instance,
                                                                            })
     
        plain_message = strip_tags(html_message)
    #send email to the user
        send_mail('Thanks for creating a Scipertise account ' + instance.first_name, plain_message, 'founders@scipertise.com', [user_email], fail_silently=False, html_message=html_message)
        mail_admins('New user sign up', instance.first_name + ' has signed up for a Scipertise account', fail_silently=False, )
        return super(SignUp, self).form_valid(form)
        
    
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


def EditProfileView(request):
    form = EditProfile()
    if request.method == 'POST' and 'save_continue' in request.POST:
        form =EditProfile(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('edit_profile'))
    if request.method =='POST' and 'save_submit' in request.POST:
        form =EditProfile(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form = EditProfile(instance = request.user)

        return render(request, 'edit_profile.html', {
            'form': form,
        })


@login_required
def EditProfileRateView(request):
    form_two =EditProfileDetail()
    if request.method == 'POST':
        form_two = EditProfileDetail(request.POST, instance =request.user)
        if form_two.is_valid():
            form_two.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form_two = EditProfileDetail(instance = request.user)
        
        return render(request, 'edit_profile_rate.html', {
            'form_two': form_two,

        })
@login_required
def EditProfileTutorialView(request):
    form_two =EditProfileDetail()
    if request.method == 'POST':
        form_two = EditProfileDetail(request.POST, instance =request.user)
        if form_two.is_valid():
            form_two.save()
        return HttpResponseRedirect(reverse('profile'))
    else:
        form_two = EditProfileDetail(instance = request.user)
        
        return render(request, 'edit_profile_tutorials.html', {
            'form_two': form_two,

        })
    
@login_required
def SubmitProfileView(request):
    form_two =EditProfileDetail()
#    form_two.instance.user = self.request.user
    if request.method == 'POST':
        form_two = EditProfileDetail(request.POST, instance =request.user)
        if form_two.is_valid():
            form_two.save()
    #send email to scipertise admin
            mail_admins('New profile submission', 'An expert profile has been submitted by ' + form_two.instance.first_name, fail_silently=False, )
        return HttpResponseRedirect(reverse('profile'))
    else:
        form_two = EditProfileDetail(instance = request.user)
        
        return render(request, 'submit_profile.html', {
            'form_two': form_two,

        })
#class SubmitProfileView(FormView):
#    model = CustomUser
#    form_two = EditProfileDetail
#    template_name = 'submit_profile.html'
#    def form_valid(self):
#        self.instance.profile_under_review = True
#        
    
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
    
