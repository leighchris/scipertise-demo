
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from users.forms import LoginForm
from django.contrib import admin
from django.contrib.auth import views as auth_views

#app_name = 'users'

urlpatterns = [
    #path('', include('booking.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('login/', auth_views.login, {'authentication_form': LoginForm}, name='login'),
    path('login/', auth_views.LoginView.as_view(), {'authentication_form': LoginForm}, name='login'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/<int:pk>/', views.view_profile, name='profile_with_pk'),
    path('profile/edit/', views.EditProfileView, name='edit_profile'),
    #path('profile/edit/skills/', views.EditSkillView, name='edit_skills')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)