from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from users.models import CustomUser

 

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, null=True, default='', on_delete=models.CASCADE)
    expert = models.ForeignKey(CustomUser, null=True, default='',on_delete=models.CASCADE, related_name='bookings')
    title = models.CharField(max_length=200, default='Title/subject of your video call', null=True)
    start_time = models.DateTimeField('Start time', null=True)
    end_time = models.DateTimeField('End time', null=True)
    notes = models.TextField('Notes', blank=True, null=True) 
    is_confirmed = models.BooleanField(blank=True, default=False)
    is_tutorial = models.BooleanField(blank=True, default=False)
    description = models.TextField('Description', blank=True, null=True) 
  
 
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        
    def get_absolute_url(self):
        return reverse('booking:booking_detail', kwargs={"pk": self.pk})
    
#class Confirmation(models.Model):
#    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
#    expert_confirming = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#    is_confirmed = models.BooleanField(default=False)
#    
#    def get_absolute_url(self):
#        return reverse('booking:booking_detail', kwargs={"pk": self.booking_id})
#    

