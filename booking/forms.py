from django.forms import ModelForm, DateInput
from booking.models import Booking
from django import forms

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'start_time': DateInput(attrs={'class': 'form-control','type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
          'end_time': DateInput(attrs={'class': 'form-control','type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
          'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = '__all__'
