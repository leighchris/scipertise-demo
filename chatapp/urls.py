from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.app, name='twilio'),
#    re_path(r'^token', views.token, name='token'),
]
    
