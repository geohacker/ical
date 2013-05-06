import sys
from icalendar import Calendar
from dateutil import parser

schedule = open(sys.argv[1])
lookfor = sys.argv[2:]

format = '%A, %d. %B %Y %I:%M%p'
filtered = Calendar()

calendar = Calendar.from_ical(schedule.read())
for event in calendar.walk():
    found = 0
    if 'SUMMARY' in event.keys():
        summary = event['SUMMARY']
        for keyword in lookfor:
            if summary.lower().find(keyword.lower()) != -1:
                found = 1
                continue
            else:
                found = 0
                break
        if found:
            start = parser.parse(event['DTSTART'].to_ical()).strftime(format)
            end = parser.parse(event['DTEND'].to_ical()).strftime(format)
            print summary
            print "From: ", start
            print "To:", end
            filtered.add_component(event)


filtered_file = open('filtered.ics', 'wb')
filtered_file.write(filtered.to_ical())
filtered_file.close()
