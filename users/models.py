from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


# Create your models here.


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    #skills = models.CharField(max_length =200, null=True, default='')
    position = models.CharField(max_length =50, null=True, default='')
    bio = models.CharField(max_length=300, null=True, default='')
    skills = TaggableManager(help_text="A comma-separated list of tags.")


class TaggedSkill(TaggedItemBase):
    content_object = models.ForeignKey('Skill', on_delete=models.DO_NOTHING)  
    
class Skill(models.Model):
    name = models.CharField(max_length =200, null=True, default='')
    #skills = models.CharField(max_length =50, null=True, default='')
    tags = TaggableManager(through=TaggedSkill)



    
    
        





        


    

    

   