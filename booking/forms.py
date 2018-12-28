from django.forms import ModelForm, DateInput
from booking.models import Booking
from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


        
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['title','start_time','end_time','notes']
        # datetime-local is a HTML5 input type, format to make date time show on fields
        labels = {
          'title': 'Please select a title for your requested video call:',
          'start_time': 'Suggested date and start time:',
          'end_time': 'Suggested end time:',
          'notes': 'Describe what you are interested in discussing in 2-3 sentences:',
        }
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'start_time': DateTimePickerInput(format="YYYY-MM-DD HH:mm"),
          'end_time': DateTimePickerInput(format="YYYY-MM-DD HH:mm"),
          'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
        help_texts = {
    
          'start_time': 'Please select a date and time during the available hours listed on the expert profile page',
          'end_time': '*Appointments cannot exceed 1 hour'
          
        }



class ConfirmForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['is_confirmed']
        # datetime-local is a HTML5 input type, format to make date time show on fields
        labels = {
          'is_confirmed': 'I confirm this video call',
        }
        


