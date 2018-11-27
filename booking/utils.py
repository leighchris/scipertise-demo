
from datetime import datetime as dtime, date, time
import datetime
from booking.models import Booking 
from datetime import datetime, timedelta
from calendar import HTMLCalendar


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td

	def formatday(self, day, booking):
		bookings_per_day = booking.filter(start_time__day=day)
		d = ''
		for booking in bookings_per_day:
			d += f'<li> {booking.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, booking):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, booking)
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