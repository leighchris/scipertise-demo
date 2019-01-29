from django.contrib import admin

# Register your models here.

from booking.models import Booking, HelpRequest
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
#from booking.utils import BookingCalendar


class BookingAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_time', 'end_time', 'notes', 'is_confirmed',]
    
admin.site.register(Booking, BookingAdmin)

class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'help_needed', ]
    
admin.site.register(HelpRequest, HelpRequestAdmin)

#class ConfirmationAdmin(admin.ModelAdmin):
#    list_display = ['booking', 'expert_confirming', 'is_confirmed',]
#    
#admin.site.register(Confirmation, ConfirmationAdmin)
#

