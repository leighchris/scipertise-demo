from django.shortcuts import render
from django.db.models import Q
from users.models import CustomUser

# Create your views here.

def search_users(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        if query is not None:
            lookups= Q(skills__name__iexact=query)
            #results= CustomUser.skill.filter(lookups).distinct()
            results = CustomUser.objects.filter(lookups).distinct()
            context={'results': results,
                     'submitbutton': submitbutton}
            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')
    
    
    #users_taggedskill_items
 