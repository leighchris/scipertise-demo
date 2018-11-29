from django.shortcuts import render
from django.db.models import Q
from users.models import CustomUser
from django.views.generic import TemplateView, DetailView, ListView
from users.models import CustomUser
from taggit.models import Tag
from functools import reduce

# Create your views here.

def search_users(request):
    if request.method == 'GET':
        query= request.GET.get('q').split()
        submitbutton= request.GET.get('submit')
        if query is not None:
            for word in query:
                lookups = Q(skills__name__icontains=word)
            results = CustomUser.objects.filter(lookups).distinct()
                #lookups= (Q(skills__name__iexact=query) | Q(skills__name__icontains=query))
                #results= CustomUser.skill.filter(lookups).distinct()
                #results = CustomUser.objects.filter(lookups).distinct()
            context={'results': results, 'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')



 