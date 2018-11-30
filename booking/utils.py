
from datetime import datetime as dtime, date, time
import datetime
from booking.models import Booking 
from datetime import datetime, timedelta
from calendar import HTMLCalendar
#
#
#class Calendar(HTMLCalendar):
#	def __init__(self, year=None, month=None, booking):
#        booking = Booking.objects.filter(user=self.request.user)
#		self.year = year
#		self.month = month
#		super(Calendar, self).__init__()

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year=year
        self.month=month
        #bookings=Booking.objects.filter(user=self.request.user)
        super(Calendar, self).__init__()
	# formats a day as a td

    def formatday(self, day, bookings):
        bookings_per_day = bookings.filter(start_time__day=day)
        d = ''
        for booking in bookings_per_day:
            d += f'<li> {booking.title} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
            return '<td></td>'

	# formats a week as a tr 
    def formatweek(self, theweek, bookings):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, bookings)
        return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
    def formatmonth(self, withyear=True):
        bookings = Booking.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, bookings)}\n'
        return cal
    
#from calendar import HTMLCalendar
#from datetime import date
#from itertools import groupby
#
#from django.utils.html import conditional_escape as esc
#
#class BookingCalendar(HTMLCalendar):
#
#    def __init__(self, bookings):
#        super(BookingCalendar, self).__init__()
#        self.bookings = self.group_by_day(bookings)
#
#    def formatday(self, day, weekday):
#        if day != 0:
#            cssclass = self.cssclasses[weekday]
#            if date.today() == date(self.year, self.month, day):
#                cssclass += ' today'
#            if day in self.bookings:
#                cssclass += ' filled'
#                body = ['<ul>']
#                for booking in self.bookings[day]:
#                    body.append('<li>')
#                    body.append('<a href="%s">' % booking.get_absolute_url())
#                    body.append(esc(booking.title))
#                    body.append('</a></li>')
#                body.append('</ul>')
#                return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
#            return self.day_cell(cssclass, day)
#        return self.day_cell('noday', '&nbsp;')
#
#    def formatmonth(self, year, month):
#        self.year, self.month = year, month
#        return super(BookingCalendar, self).formatmonth(year, month)
#
#    def group_by_day(self, bookings):
#        field = lambda booking: booking.performed_at.day
#        return dict(
#            [(day, list(items)) for day, items in groupby(bookings, field)]
#        )
#
#    def day_cell(self, cssclass, body):
#        return '<td class="%s">%s</td>' % (cssclass, body)