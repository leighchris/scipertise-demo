from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
 

# Create your models here.

class Booking(models.Model):
    title = models.CharField(max_length=200, default='Video Call', null=True)
    start_time = models.DateTimeField('Start time')
    end_time = models.DateTimeField('End time')
    notes = models.TextField('Notes', help_text='Please provide some detail on what you would like to learn or discuss', blank=True, null=True)
 
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
