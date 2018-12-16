
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static
from users.forms import LoginForm
from django.contrib import admin
from django.contrib.auth import views as auth_views
from booking.views import BookingView, BookingUpdateView
from . import views


urlpatterns = [
    #path('', include('booking.urls')),
    path('session/', views.session_view),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)