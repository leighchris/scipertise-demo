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

from django.template.loader import render_to_string
from django.utils.html import strip_tags


class BookingView(CreateView):
    model = Booking
    form_class = BookingForm
    def form_valid(self, form):
        booking = form.save(commit=False)
        form.instance.user = self.request.user
        form.instance.expert = CustomUser.objects.get(id=self.kwargs.get('pk'))
#        user_email = form.instance.user.email
#        expert_email = form.instance.expert.email
#
#        html_message = render_to_string('booking_request_email_user.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert})
#        html_message_expert = render_to_string('booking_request_email_expert.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        plain_message = strip_tags(html_message)
#        plain_message_expert = strip_tags(html_message_expert)
#    #send email to the user
#        send_mail('Thanks for your booking request ' + form.instance.user.first_name, plain_message, 'founders@scipertise.com', [user_email], fail_silently=False, html_message=html_message)
#    #send email to the expert
#        send_mail(form.instance.user.first_name + " has requested a video call with you", plain_message_expert, 'founders@scipertise.com', [expert_email], fail_silently=False, html_message=html_message_expert)
        return super(BookingView, self).form_valid(form)

    
class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    def form_valid(self, form):
        booking = Booking.objects.get(id=self.kwargs.get('pk'))
        form.instance.user = booking.user
        form.instance.expert = booking.expert
#        user_email = form.instance.user.email
#        expert_email = form.instance.expert.email
#        html_message = render_to_string('update_booking_user.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        html_message_expert = render_to_string('update_booking_expert.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        plain_message = strip_tags(html_message)
#        plain_message_expert = strip_tags(html_message_expert)
#    #send email to the user
#        send_mail('Your Scipertise booking request has been changed', plain_message, 'founders@scipertise.com', [user_email], fail_silently=False, html_message=html_message)
#    #send email to the expert
#        send_mail('Your Scipertise booking request has been changed', plain_message_expert, 'founders@scipertise.com', [expert_email], fail_silently=False, html_message=html_message_expert)
        return super(BookingUpdateView, self).form_valid(form)

    
class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        booking = Booking.objects.get(id=self.kwargs.get('pk'))
        form.instance.user = booking.user
        form.instance.expert = booking.expert
#        user_email = form.instance.user.email
#        expert_email = form.instance.expert.email
#        html_message = render_to_string('delete_booking_user.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        html_message_expert = render_to_string('delete_booking_expert.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        plain_message = strip_tags(html_message)
#        plain_message_expert = strip_tags(html_message_expert)
#    #send email to the user
#        send_mail('Your Scipertise booking has been cancelled', plain_message, 'founders@scipertise.com', [user_email], fail_silently=False, html_message=html_message)
#    #send email to the expert
#        send_mail('Your Scipertise booking has been cancelled', plain_message_expert, 'founders@scipertise.com', [expert_email], fail_silently=False, html_message=html_message_expert)
        return super(BookingUpdateView, self).form_valid(form)

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
#    def form_valid(self, form):
#        booking = Booking.objects.get(id=self.kwargs.get('pk'))
#        form.instance.user = booking.user
#        form.instance.expert = booking.expert
#        user_email = form.instance.user.email
#        expert_email = form.instance.expert.email
#        html_message = render_to_string('confirm_booking_user.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        html_message_expert = render_to_string('confirm_booking_expert.html', {'user': form.instance.user,
#                                                                            'expert': form.instance.expert,
#                                                                            'booking': booking,
#                                                                            })
#        plain_message = strip_tags(html_message)
#        plain_message_expert = strip_tags(html_message_expert)
#    #send email to the user
#        send_mail('Your Scipertise booking has been confirmed', plain_message, 'founders@scipertise.com', [user_email], fail_silently=False, html_message=html_message)
#    #send email to the expert
#        send_mail('Your Scipertise booking has been confirmed', plain_message_expert, 'founders@scipertise.com', [expert_email], fail_silently=False, html_message=html_message_expert)
#        return super(ConfirmView, self).form_valid(form)
    
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
