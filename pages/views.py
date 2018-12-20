from django.shortcuts import render
from django.views.generic import TemplateView, ListView


# Create your views here.



    
    
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    
def error_404_view(request, exception):
    data = {"name": "scipertise.com"}
    return render(request,'custom_404.html', data)