import json
import datetime

from flask import Flask, render_template

def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered

def get_config(key):
    with open('settings.json') as json_data_file:
        settings = json.load(json_data_file)
        return settings[key]


def write_config(key, value):
    with open('settings.json') as json_data_file:
        settings = json.load(json_data_file)
    settings[key] = value
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile)
    return

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

def close_box():
     os.system("python ~/close_box.py")
     write_config("box_status", "closed")


def open_box():
    os.system("python ~/close_box.py")
    tools.write_config("box_status", "open")
