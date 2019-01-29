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
from booking.models import Booking, HelpRequest
from booking.forms import BookingForm, ConfirmForm, GroupForm, RequestExpertForm

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.messages.views import SuccessMessageMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expert'] = CustomUser.objects.get(id=self.kwargs.get('pk'))
        return context
    

class GroupView(CreateView):
    model = Booking
    form_class = GroupForm
    template_name = 'booking/group_form.html'
    def form_valid(self, form):
        booking = form.save(commit=False)
        form.instance.user = self.request.user
        form.instance.expert = CustomUser.objects.get(id=self.kwargs.get('pk'))
        form.instance.is_tutorial = True
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
        return super(GroupView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expert'] = CustomUser.objects.get(id=self.kwargs.get('pk'))
        return context

    
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
    def form_valid(self, form):
        booking = Booking.objects.get(id=self.kwargs.get('pk'))
        form.instance.user = booking.user
        form.instance.expert = booking.expert
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
        return super(ConfirmView, self).form_valid(form)
    
class RequestExpertView(SuccessMessageMixin, CreateView):
    model = HelpRequest
    form_class = RequestExpertForm
    template_name = 'booking/request_expert_form.html'
    success_message = 'Thanks! Your request has been submitted.'
    def form_valid(self, form):
        help_request = form.save(commit=False)
        form.instance.user = self.request.user
        return super(RequestExpertView, self).form_valid(form)

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['expert'] = CustomUser.objects.get(id=self.kwargs.get('pk'))
#        return context
    
