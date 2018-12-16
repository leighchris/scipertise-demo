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
from django.core.mail import send_mail

from users.forms import CustomUserCreationForm, EditProfile
from users.models import CustomUser
#from booking.utils import Calendar
from booking.models import Booking
from booking.forms import BookingForm, ConfirmForm

##OpenTok Test
#
#from opentok import OpenTok
#opentok = OpenTok(api_key, api_secret)
## Create a session that attempts to send streams directly between clients (falling back
## to use the OpenTok TURN server to relay streams if the clients cannot connect):
#session = opentok.create_session()
#
#from opentok import MediaModes
## A session that uses the OpenTok Media Router, which is required for archiving:
#session = opentok.create_session(media_mode=MediaModes.routed)
#
## An automatically archived session:
#session = opentok.create_session(media_mode=MediaModes.routed, archive_mode=ArchiveModes.always)
#
## A session with a location hint
#session = opentok.create_session(location=u'12.34.56.78')
#
## Store this session ID in the database
#session_id = session.session_id
#
## Generate a Token from just a session_id (fetched from a database)
#token = opentok.generate_token(session_id)
#
## Generate a Token by calling the method on the Session (returned from create_session)
#token = session.generate_token()
#
#from opentok import Roles
## Set some options in a token
#token = session.generate_token(role=Roles.moderator,
#                               expire_time=int(time.time()) + 10,
#                               data=u'name=Johnny'
#                               initial_layout_class_list=[u'focus'])
#
#archive = opentok.start_archive(session_id, name=u'Important Presentation', output_mode=OutputModes.individual)
#
## Store this archive_id in the database
#archive_id = archive.id
#



class BookingView(CreateView):
    model = Booking
    form_class = BookingForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.expert = CustomUser.objects.get(id=self.kwargs.get('pk'))
        user_email = form.instance.user.email
        expert_email = form.instance.expert.email
        msg = 'Thanks for requesting a video chat' + form.instance.user.first_name + '. We will notify you when your booking is confirmed.'
        msg_expert = 'Someone has requested a video chat with you'
        send_mail('Thanks for your booking request ' + form.instance.user.first_name, msg, 'founders@scipertise.com',
        [user_email], fail_silently=False)
        send_mail('Someone has requested a video chat with you', msg_expert, 'founders@scipertise.com',
        [expert_email], fail_silently=False)
        return super(BookingView, self).form_valid(form)
    
class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        form.instance.expert = CustomUser.objects.get(id=self.kwargs.get('pk'))
#        user_email = form.instance.user.email
#        expert_email = form.instance.expert.email
#        msg = 'Thanks for requesting a video chat' + form.instance.user.first_name + '. We will notify you when your booking is confirmed.'
#        msg_expert = form.instance.user.first_name + ' has made a change to their booking request'
#        send_mail('Thanks for your booking request ' + form.instance.user.first_name, msg, 'founders@scipertise.com',
#        [user_email], fail_silently=False)
#        send_mail(form.instance.user.first_name + ' has requested a change to their booking request', msg_expert, 'founders@scipertise.com',
#        [expert_email], fail_silently=False)
#        return super(BookingView, self).form_valid(form)
    
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
