"""scipertise_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'booking'

urlpatterns = [
    path('users/', include('users.urls')),
    path('users/profile/<int:pk>/booking/', views.BookingView.as_view(), name='user_booking_new'),
    path('booking/', views.BookingListView.as_view(), name="booking_list"),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name="booking_detail"),
    path('booking/edit/<int:pk>/', views.BookingUpdateView.as_view(), name="booking_update"),
    path('booking/delete/<int:pk>/', views.BookingDeleteView.as_view(), name="booking_delete"),
    path('booking/confirm/<int:pk>', views.ConfirmView.as_view(), name='confirm_booking'),
#    path('users/profile/<int:pk>/booking/<int:pk>/', views.BookingDetailView.as_view(), name="booking_detail"),
#    path('users/profile/<int:pk>/booking/edit/<int:pk>/', views.BookingUpdateView.as_view(), name="booking_update"),
#    path('booking/edit/<int:pk>/booking/delete/<int:pk>/', views.BookingDeleteView.as_view(), name="booking_delete"),
 
 
]



    #path('users/profile/booking/', views.CalendarView.as_view(), name='calendar'),
    #path('booking/calendar/', views.calendar, name='new_calendar'),