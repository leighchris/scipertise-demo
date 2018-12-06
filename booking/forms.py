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
          'title': 'Name for the video chat:',
          'start_time': 'Suggested date and time:',
          'end_time': 'Suggested end time:',
          'notes': 'Prove 2-3 sentences on what you would like to discuss:',
        }
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'start_time': DateTimePickerInput(format="YYYY-MM-DD HH:mm"),
          'end_time': DateTimePickerInput(format="YYYY-MM-DD HH:mm"),
          'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
#        fields = '__all__'
#
#    def __init__(self, *args, **kwargs):
#        super(BookingForm, self).__init__(*args, **kwargs)
#        # input_formats to parse HTML5 datetime-local input to datetime field
#        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
#        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

