from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, TemplateView, DetailView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from calendar import HTMLCalendar
import calendar

from users.forms import CustomUserCreationForm, EditProfile
from users.models import CustomUser
#from booking.utils import Calendar
from booking.models import Booking
from booking.forms import BookingForm, ConfirmForm

class BookingView(CreateView):
    model = Booking
    form_class = BookingForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.expert = CustomUser.objects.get(id=self.kwargs.get('pk'))
        return super(BookingView, self).form_valid(form)
    
class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    
class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('profile')

class BookingListView(ListView):
    model = Booking
    context_object_name = 'booking_list'
    template = 'templates/booking_list.html'
    
    def get_queryset(self):
        bookings = Booking.objects.filter(user=self.request.user)
        return bookings

    
class BookingDetailView(DetailView):
    model = Booking
    template = 'templates/booking_detail.html'
    

        
#def is_confirmed(request, pk):
#    form = ConfirmForm()
#    if request.method == 'POST':
#        form = ConfirmForm(request.POST,
#            expert_confirming = request.user, 
#            booking = get_object_or_404(Booking, pk=booking.pk),
#            is_confirmed = True
#            )
#        if form.is_valid():
#            form.save()
#        return HttpResponseRedirect(reverse('booking:booking_detail'))
#    else:
#        return render(request, 'confirm_booking.html', {'form': form})
    
class ConfirmView(UpdateView):
    model = Booking
    form_class = ConfirmForm
    template = 'templates/confirmation_form.html'
    def form_valid(self, form):
        return super(ConfirmView, self).form_valid(form)
    
#@login_required
#def EditProfileView(request):
#    form = EditProfile()
#    if request.method == 'POST':
#        form = EditProfile(request.POST, instance =request.user)
#        if form.is_valid():
#            form.save()
#        return HttpResponseRedirect(reverse('profile'))
#    else:
#        form = EditProfile(instance = request.user)
#        return render(request, 'edit_profile.html', {'form': form})

#class CalendarView(generic.ListView):
#    model = Booking
#    template_name = 'calendar.html'
#    
#    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data()
#
#
#        # use today's date for the calendar
#        d = get_date(self.request.GET.get('day', None))
#      
#        # Instantiate our calendar class with today's year and date
#        cal = Calendar(d.year, d.month)
#
#        # Call the formatmonth method, which returns our calendar as a table
#        html_cal = cal.formatmonth(withyear=True)
#        context['calendar'] = mark_safe(html_cal)
#        d = get_date(self.request.GET.get('month', None))
#        context['prev_month'] = prev_month(d)
#        context['next_month'] = next_month(d)
#      
#        return context
#    
#
#    
#def get_date(req_day):
#    if req_day:
#        year, month = (int(x) for x in req_day.split('-'))
#        return date(year, month, day=1)
#    return datetime.today()
#        
#
#def prev_month(d):
#    first = d.replace(day=1)
#    prev_month = first - timedelta(days=1)
#    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#    return month
#
#def next_month(d):
#    days_in_month = calendar.monthrange(d.year, d.month)[1]
#    last = d.replace(day=days_in_month)
#    next_month = last + timedelta(days=1)
#    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#    return month

#
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


#    def get_queryset(self, pk=None):
#        if pk:
#            user = CustomUser.objects.get(pk=pk)
#        else:
#            user = self.request.user
#        bookings = Booking.objects.filter(expert=user)
#        return bookings
#
##
