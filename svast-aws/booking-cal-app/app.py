from flask import Flask, render_template
from datetime import datetime
from datetime import timedelta
import requests
import icalendar
import serverless_wsgi


app = Flask(__name__)

def format_date(date):
    return date.strftime("%Y-%m-%d")
# ("%Y-%m-%dT%H:%M:%S")

@app.route('/')
def index():
    ical_url_app_1 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=82833dc5-c2cd-4ef2-8ddb-e2085c967585'
    ical_url_app_2 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=06f91d84-41a4-46f0-9fe9-b478e494c6cd'
    ical_url_app_3 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=405911af-1336-46e0-bb73-826f7bb0ecf0'
    ical_url_app_4 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=b0e27f8a-ead1-4f31-b755-e64625a16906'
    ical_url_app_5 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=7dc278c3-b735-4c31-ac24-f391bcfa4dc7'
    ical_url_app_6 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=ef5a41c6-29f6-4e07-aca3-129d8e9eedf3'
    ical_url_app_7 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=ed45ddf8-9c2d-40cd-b636-e1539157e0be'
    ical_url_app_8 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=96192e45-89d9-4b5f-98d5-ba4c7ac72246'

    response_app_1 = requests.get(ical_url_app_1)
    response_app_2 = requests.get(ical_url_app_2)
    response_app_3 = requests.get(ical_url_app_3)
    response_app_4 = requests.get(ical_url_app_4)
    response_app_5 = requests.get(ical_url_app_5)
    response_app_6 = requests.get(ical_url_app_6)
    response_app_7 = requests.get(ical_url_app_7)
    response_app_8 = requests.get(ical_url_app_8)

    cal_app_1 = icalendar.Calendar.from_ical(response_app_1.text)
    cal_app_2 = icalendar.Calendar.from_ical(response_app_2.text)
    cal_app_3 = icalendar.Calendar.from_ical(response_app_3.text)
    cal_app_4 = icalendar.Calendar.from_ical(response_app_4.text)
    cal_app_5 = icalendar.Calendar.from_ical(response_app_5.text)
    cal_app_6 = icalendar.Calendar.from_ical(response_app_6.text)
    cal_app_7 = icalendar.Calendar.from_ical(response_app_7.text)
    cal_app_8 = icalendar.Calendar.from_ical(response_app_8.text)

    events = []
    for component in cal_app_1.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 1 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#f6993f'
            }
            events.append(event)
    
    for component in cal_app_2.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 2 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#800000'
            }
            events.append(event)
    
    for component in cal_app_3.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 3 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#38c172'
            }
            events.append(event)
    
    for component in cal_app_4.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 4 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#4dc0b5'
            }
            events.append(event)
    
    for component in cal_app_5.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 5 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#3490dc'
            }
            events.append(event)
    
    for component in cal_app_6.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 6 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#6574cd'
            }
            events.append(event)
    
    for component in cal_app_7.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 7 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#9561e2'
            }
            events.append(event)
    
    for component in cal_app_8.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 8 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#f66d9b'
            }
            events.append(event)

    return render_template('index.html', events=events, timestamp=datetime.now())

@app.route('/app/1')
def availability1():
    ical_url_app_1 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=82833dc5-c2cd-4ef2-8ddb-e2085c967585'

    response_app_1 = requests.get(ical_url_app_1)

    cal_app_1 = icalendar.Calendar.from_ical(response_app_1.text)

    events = []
    for component in cal_app_1.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 1 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#f6993f'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/2')
def availability2():
    ical_url_app_2 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=06f91d84-41a4-46f0-9fe9-b478e494c6cd'

    response_app_2 = requests.get(ical_url_app_2)

    cal_app_2 = icalendar.Calendar.from_ical(response_app_2.text)

    events = []
    for component in cal_app_2.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 2 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#800000'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/3')
def availability3():
    ical_url_app_3 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=405911af-1336-46e0-bb73-826f7bb0ecf0'

    response_app_3 = requests.get(ical_url_app_3)

    cal_app_3 = icalendar.Calendar.from_ical(response_app_3.text)

    events = []
    for component in cal_app_3.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 3 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#38c172'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/4')
def availability4():
    ical_url_app_4 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=b0e27f8a-ead1-4f31-b755-e64625a16906'

    response_app_4 = requests.get(ical_url_app_4)

    cal_app_4 = icalendar.Calendar.from_ical(response_app_4.text)

    events = []
    for component in cal_app_4.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 4 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#4dc0b5'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/5')
def availability5():
    ical_url_app_5 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=7dc278c3-b735-4c31-ac24-f391bcfa4dc7'

    response_app_5 = requests.get(ical_url_app_5)

    cal_app_5 = icalendar.Calendar.from_ical(response_app_5.text)

    events = []
    for component in cal_app_5.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 5 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#3490dc'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/6')
def availability6():
    ical_url_app_6 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=ef5a41c6-29f6-4e07-aca3-129d8e9eedf3'

    response_app_6 = requests.get(ical_url_app_6)

    cal_app_6 = icalendar.Calendar.from_ical(response_app_6.text)

    events = []
    for component in cal_app_6.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 6 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#6574cd'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/7')
def availability7():
    ical_url_app_7 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=ed45ddf8-9c2d-40cd-b636-e1539157e0be'

    response_app_7 = requests.get(ical_url_app_7)

    cal_app_7 = icalendar.Calendar.from_ical(response_app_7.text)

    events = []
    for component in cal_app_7.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 7 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#9561e2'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

@app.route('/app/8')
def availability8():
    ical_url_app_8 = 'https://admin.booking.com/hotel/hoteladmin/ical.html?t=96192e45-89d9-4b5f-98d5-ba4c7ac72246'

    response_app_8 = requests.get(ical_url_app_8)

    cal_app_8 = icalendar.Calendar.from_ical(response_app_8.text)

    events = []
    for component in cal_app_8.walk():
        if component.name == 'VEVENT':
            event = {
                'title': "APP 8 ",
                'start': format_date(component.get('dtstart').dt),
                'end': format_date(component.get('dtend').dt + timedelta(days=1)),
                'backgroundColor': '#f66d9b'
            }
            events.append(event)

    return render_template('detail.html', events=events, timestamp=datetime.now())

if __name__ == '__main__':
    app.run()

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)