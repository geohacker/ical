import sys
from icalendar import Calendar

schedule = open(sys.argv[1])
lookfor = [key.lower() for key in sys.argv[2:]]

format = '%A, %d. %B %Y %I:%M%p'
filtered = Calendar()

calendar = Calendar.from_ical(schedule.read())
for event in calendar.walk():
    if 'SUMMARY' in event.keys():
        summary = event['SUMMARY'].lower()
        if any(key in summary for key in lookfor):
            msg = []
            if 'RRULE' in event and 'FREQ' in event['RRULE']:
                msg.extend(event['RRULE']['FREQ'])
            else:
                msg.append(event['DTSTART'].to_ical())
            msg.append(event['SUMMARY'])
            print ' '.join(msg)
            filtered.add_component(event)


filtered_file = open('filtered.ics', 'wb')
filtered_file.write(filtered.to_ical())
filtered_file.close()
