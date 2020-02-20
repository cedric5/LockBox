import json
import datetime
import os
import urllib.request
from flask import Flask, render_template


def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered

def has_internet_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

def get_config(key):
    try:
        with open('settings.json') as json_data_file:
            settings = json.load(json_data_file)
        return settings[key]
    except:
        recover_config()


def write_config(key, value):
    try:
        with open('settings.json') as json_data_file:
            settings = json.load(json_data_file)
            settings[key] = value
        with open('settings.json', 'w') as outfile:
            json.dump(settings, outfile)
            return
    except:
        recover_config()

def config_is_set(key):
    if not get_config(key):
        return False
    else:
        return True


def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours, minutes, seconds)


def time_left(box_status):
    open_close_time = ""
    if box_status == "closed": open_close_time = get_config('open_time')
    if box_status == "open": open_close_time = get_config('close_time')
    if open_close_time == "": return 0, 0, 0, 0
    time_to_compare = datetime.datetime.strptime(open_close_time, '%Y-%m-%d %H:%M')
    now = datetime.datetime.now()
    return daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, time_to_compare))


def get_next_friday():
    next_friday = datetime.date.today()
    while next_friday.weekday() != 4:
        next_friday += datetime.timedelta(1)

    return datetime.datetime(next_friday.year, next_friday.month, next_friday.day, hour=18, minute=0, second=0)

def create_settings():
    try:
        print('creating settings.json')
        f = open("settings.json", "x")
        f.close()
        f = open("settings.json", "w+")
        f.write("{\"close_time\": \"\", \"open_time\": \"\", \"wifi_wpa2\": \"JEEEJ\", \"mode\": \"manual\", "
                "\"wifi_strength\": 5, \"wifi_ssid\": \"EchtGoeieWifiMaat\", \"box_status\": \"open\"}")
        f.close()
    except IOError:
        print('settings file not accesible ')

def recover_config():
    os.system("rm -f settings.json")
    create_settings()
    #os.system('sudo shutdown -r now')
