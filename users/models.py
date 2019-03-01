from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.conf import settings
from chatapp.utils import get_client

# Create your models here.


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    position = models.CharField(max_length =10000, null=True, default='', blank=True)
    bio = models.CharField(max_length =10000, null=True, default='', blank=True)
    skills = TaggableManager(help_text="A comma-separated list of tags.")
    image = models.ImageField(upload_to="profile_image", blank=True)
    website = models.CharField(max_length=10000, null=True, default='', blank=True)
    skill_area1_title = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area1 = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area2_title = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area2 = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area3_title = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area3 = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area4_title = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area4 = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area5_title = models.CharField(max_length =10000, null=True, default='', blank=True)
    skill_area5 = models.CharField(max_length =10000, null=True, default='', blank=True)
    software_hardware = models.CharField(max_length =10000, null=True, default='', blank=True)
    software_hardware_intermediate = models.CharField(max_length =10000, null=True, default='', blank=True)
    availability = models.CharField(max_length=10000, null=True, default='', blank=True)
    rate = models.CharField(max_length= 10000, null=True, default='', blank=True)
    expert = models.BooleanField(blank=True, default=False)
    gives_tutorials = models.BooleanField(blank=True, default=False)
    tutorial_area = models.CharField(max_length =10000, null=True, default='', blank=True)
    wants_expert = models.BooleanField(blank=True, default=False)
    needs_help_with = models.CharField(max_length =10000, null=True, default='', blank=True)
    profile_under_review = models.BooleanField(blank=True, default=False)
    profile_approved = models.BooleanField(blank=True, default=False)
    twilio_user_id = models.CharField(max_length=50, null=True)
    
    def get_chat_url(self):
        # {% for user in users %}
        # <a href='{% url "twilio-create-channel" to_user_id=user.id}'
        # <a href='{{user.get_chat_url}}'>Chat with {{user.username}}</a>
        # {$ endfor %}
        return reverse('twilio-create-channel', kwargs={'to_user_id': self.pk})

    def get_twilio_user_id(self):
        if not self.twilio_user_id:
            user = get_client().chat.services(settings.TWILIO_CHAT_SID) \
                      .users \
                      .create(identity=self.username)
            
            # import pdb; pdb.set_trace() <-- learn me
            self.twilio_user_id = user.sid
            self.save()
        return self.username
#class TaggedSkill(TaggedItemBase):
#    content_object = models.ForeignKey('Skill', on_delete=models.DO_NOTHING)  
#    
#class Skill(models.Model):
#    name = models.CharField(max_length =200, null=True, default='')
#    #skills = models.CharField(max_length =50, null=True, default='')
#    tags = TaggableManager(through=TaggedSkill)



    
    
        





        


    

    

   