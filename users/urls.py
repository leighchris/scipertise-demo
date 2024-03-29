
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static
from users.forms import LoginForm
from django.contrib import admin
from django.contrib.auth import views as auth_views
from booking.views import BookingView, BookingUpdateView


urlpatterns = [
    #path('', include('booking.urls')),
    path('', include('django.contrib.auth.urls')),
#    path('search/', include('haystack.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), {'authentication_form': LoginForm}, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('profile/', views.view_profile, name='profile'),
    path('profile/<int:pk>/', views.view_profile, name='profile_with_pk'),
    path('profile/edit/', views.EditProfileView, name='edit_profile'),
    path('profile/edit/rate/', views.EditProfileRateView, name='edit_profile_rate'),
    path('profile/edit/tutorials/', views.EditProfileTutorialView, name='edit_profile_tutorials'),
    path('profile/edit/submit/', views.SubmitProfileView, name='submit_profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('browse/', views.BrowseView.as_view(), name='browse'),
    path('profile/image/', views.EditProfileImageView, name='edit_profile_image'),
    path('skills/<slug>/', views.SkillView.as_view(), name='skills'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)