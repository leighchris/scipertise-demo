from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('faq/', views.FAQView.as_view(), name='faq'),
   
]