#--------TEST GOOGLE CALENDER API--------  
# k_3gA4K5ViUFXghH8f3iyATY
#1078313357944-g5urm7a73e5clo4pevl18rnqg4t2sl7m.apps.googleusercontent.com

from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools



"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
store = file.Storage('token.json')
creds = store.get()
 
    
service = build('calendar', 'v3', http=creds.authorize(Http()))

page_token = None
while True:
  calendar_list = service.calendarList().list(pageToken=page_token).execute()
  for calendar_list_entry in calendar_list['items']:
    print(calendar_list_entry['summary'])
  page_token = calendar_list.get('nextPageToken')
  if not page_token:
    break


# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                    maxResults=10, singleEvents=True,
                                    orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])


