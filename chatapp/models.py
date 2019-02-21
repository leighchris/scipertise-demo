from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Channel(models.Model):
    twilio_chat_id = models.CharField(max_length=50)
    channel_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    users = models.ManyToManyField(get_user_model())
    created_at = models.DateTimeField(auto_now_add=True)
    last_message_at = models.DateTimeField(auto_now=True)