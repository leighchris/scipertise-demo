
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView, name='edit_profile'),
    #path('profile/edit/skills/', views.EditSkillView, name='edit_skills')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)