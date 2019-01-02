from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


# Create your models here.


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    position = models.CharField(max_length =200, null=True, default='', blank=True)
    bio = models.CharField(max_length=400, null=True, default='', blank=True)
    skills = TaggableManager(help_text="A comma-separated list of tags.")
    image = models.ImageField(upload_to="profile_image", blank=True)
    website = models.CharField(max_length=200, null=True, default='', blank=True)
    skill_area1_title = models.CharField(max_length=200, null=True, default='', blank=True)
    skill_area1 = models.CharField(max_length=400, null=True, default='', blank=True)
    skill_area2_title = models.CharField(max_length=200, null=True, default='', blank=True)
    skill_area2 = models.CharField(max_length=400, null=True, default='', blank=True)
    skill_area3_title = models.CharField(max_length=200, null=True, default='', blank=True)
    skill_area3 = models.CharField(max_length=400, null=True, default='', blank=True)
    skill_area4_title = models.CharField(max_length=200, null=True, default='', blank=True)
    skill_area4 = models.CharField(max_length=400, null=True, default='', blank=True)
    skill_area5_title = models.CharField(max_length=200, null=True, default='', blank=True)
    skill_area5 = models.CharField(max_length=400, null=True, default='', blank=True)
    software_hardware = models.CharField(max_length=400, null=True, default='', blank=True)
    availability = models.CharField(max_length=200, null=True, default='', blank=True)
    rate = models.CharField(max_length=100, null=True, default='', blank=True)
    expert = models.BooleanField(blank=True, default=False)
    gives_tutorials = models.BooleanField(blank=True, default=False)
    tutorial_area = models.CharField(max_length=400, null=True, default='', blank=True)
    

#class TaggedSkill(TaggedItemBase):
#    content_object = models.ForeignKey('Skill', on_delete=models.DO_NOTHING)  
#    
#class Skill(models.Model):
#    name = models.CharField(max_length =200, null=True, default='')
#    #skills = models.CharField(max_length =50, null=True, default='')
#    tags = TaggableManager(through=TaggedSkill)



    
    
        





        


    

    

   