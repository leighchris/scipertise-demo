from haystack import indexes
from users.models import CustomUser
from taggit.forms import *
from elasticsearch_dsl.connections import connections

#connections.create_connection()


class CustomUserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    position = indexes.CharField()
    bio = indexes.CharField()
    skills = indexes.MultiValueField()
#    image = indexes.ImageField()
    skill_area1_title = indexes.CharField()
    skill_area1 = indexes.CharField()
    skill_area2_title = indexes.CharField()
    skill_area2 = indexes.CharField()
    skill_area3_title = indexes.CharField()
    skill_area3 = indexes.CharField()
    skill_area4_title = indexes.CharField()
    skill_area4 = indexes.CharField()
    skill_area5_title = indexes.CharField()
    skill_area5 = indexes.CharField()
    software_hardware = indexes.CharField()
    availability = indexes.CharField()
    rate = indexes.CharField()
    expert = indexes.BooleanField()
    gives_tutorials = indexes.BooleanField()
    tutorial_area = indexes.CharField()
    

    def get_model(self):
        return CustomUser

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    
    def prepare_tags(self, obj):
        return [skill.name for skill in obj.skills.all()]