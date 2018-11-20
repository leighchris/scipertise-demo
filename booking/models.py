from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
 

# Create your models here.

class Booking(models.Model):
    title = models.CharField(max_length=200, default='', null=True)
    start_time = models.DateTimeField('Starting time', help_text='Starting time')
    end_time = models.DateTimeField('End time', help_text='End time')
    notes = models.TextField('Textual Notes', help_text='Textual Notes', blank=True, null=True)
 
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
