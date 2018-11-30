from django.forms import ModelForm, DateInput
from booking.models import Booking
from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


#class BookingForm(ModelForm):
#    class Meta:
#        model = Booking
#        # datetime-local is a HTML5 input type, format to make date time show on fields
#        widgets = {
#          'title': forms.TextInput(),
#          'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#          'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
#          'notes': forms.TextInput(attrs={'class': 'form-control'}),
#        }
#        fields = '__all__'
        
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['expert','title','start_time','end_time','notes']
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'start_time': DateTimePickerInput(format="YYYY-MM-DD HH:mm"),
          'end_time': DateTimePickerInput(format="YYYY-MM-DD HH:mm"),
          'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }
#        fields = '__all__'
#
#    def __init__(self, *args, **kwargs):
#        super(BookingForm, self).__init__(*args, **kwargs)
#        # input_formats to parse HTML5 datetime-local input to datetime field
#        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

