from django.urls import path, re_path
from . import views

app_name = 'chatapp'

urlpatterns = [
    path('<int:pk>', views.app, name='twilio'),
    path('create/<int:to_user_id>', views.create_channel, name='twilio-create-channel'),
    path('token', views.token, name='token'),
]
    
