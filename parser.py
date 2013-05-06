import os, sys
from icalendar import Calendar
from dateutil import parser

schedule = open(sys.argv[1])
lookfor = sys.argv[2]
format = '%A, %d. %B %Y %I:%M%p'

calendar = Calendar.from_ical(schedule.read())
for event in calendar.walk():
	if event.has_key('SUMMARY'):
		summary = event['SUMMARY']
		if summary.lower().find(lookfor.lower()) != -1:
			start = parser.parse(event['DTSTART'].to_ical()).strftime(format)
			end = parser.parse(event['DTEND'].to_ical()).strftime(format)
			print summary
			print "From: ", start
			print "To:", end