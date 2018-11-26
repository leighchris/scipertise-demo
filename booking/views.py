from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from calendar import HTMLCalendar
import calendar

from users.forms import CustomUserCreationForm, EditProfile
from users.models import CustomUser
from booking.utils import Calendar
from booking.models import Booking
from booking.forms import BookingForm

class CalendarView(generic.ListView):
    model = Booking
    template_name = 'calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
#    def get_queryset(self):
#        return Booking.objects.filter(user=self.request.user)
    
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
        

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


#def booking_view(request, booking_pk=None, user_pk=None):
#    instance = Booking()
#    if booking_pk:
#        instance = get_object_or_404(Booking, user_id = user_pk, pk=booking_pk)
#    else:
#        instance = Booking()
#    
#    form = BookingForm(request.POST or None)
#    if request.POST and form.is_valid():
#        form.save()
#        return HttpResponseRedirect(reverse('booking:calendar'))
#    return render(request, 'booking.html', {'form': form})

class BookingView(CreateView):
    model = Booking
    form_class = BookingForm
    #fields= ("user", "expert", "title", "start_time", "end_time", "notes")

class BookingListView(ListView):
    model = Booking
    context_object_name = 'bookings'
    template = 'templates/booking_list.html'

    
class BookingDetailView(DetailView):
    model = Booking
    template = 'templates/booking_detail.html'
    
    


    
