from django.contrib import admin

# Register your models here.

from booking.models import Booking
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
#from booking.utils import BookingCalendar


class BookingAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'notes']
    
admin.site.register(Booking, BookingAdmin)
