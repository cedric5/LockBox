import json
from datetime import date
from flask import Flask, render_template
from flask import request
from dateutil import parser
import pdb
# from flask_debug import Debug
import os
import datetime

app = Flask(__name__)


def write_config(key, value):
    with open('settings.json') as json_data_file:
        settings = json.load(json_data_file)
    settings[key] = value
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile)
    return


def get_config(key):
    with open('settings.json') as json_data_file:
        settings = json.load(json_data_file)
        return settings[key]


def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered


def time_left(box_status):
    open_close_date = parser.parse(get_config(box_status + '_time'))
    today = datetime.datetime.now()
    if box_status == "closed":
        delta = today - open_close_date
    elif box_status == "open":
        delta = open_close_date - today
    else:
        return "error date not set"
    hours = delta.seconds / 3600
    seconds = (delta.microseconds / 1000) / 1000
    return str(delta.days) + ' days ' + str(round(hours)) + ' hours and ' + str(round(seconds)) + ' seconds'


@app.route("/")
def show_main_page():
    box_status = get_config("box_status")
    open_close_time = get_config(box_status + '_time')
    time_left_days = time_left(box_status)

    template_data = {
        'content': render_page("status", {'box_status': get_config("box_status"), 'open_close_time': open_close_time,
                                          "time_left": time_left_days})
    }

    return render_template('main.html', **template_data)


def render_status_page():
    template_data = {
        'box_status': 'closed',
    }
    rendered = render_template('status.html', **template_data)
    return rendered


@app.route("/wifi")
def show_wifi_page():
    template_data = {
        'content': render_page("wifi-settings",
                               {'wifi_ssid': get_config('wifi_ssid'), 'wifi_wpa2': get_config('wifi_wpa2')})
    }
    return render_template('main.html', **template_data)


@app.route("/reboot")
def show_reboot_page():
    content_html = open("templates/reboot.html").read()
    template_data = {
        'content': content_html
    }
    return render_template('main.html', **template_data)


@app.route("/open-close")
def open_close():
    content_html = open("templates/open-close-settings.html").read()
    template_data = {
        'content': content_html
    }
    return render_template('main.html', **template_data)


@app.route("/open-box")
def open_box():
    os.system("~/open_box.py")
    return "Box open script called"


@app.route("/close-box")
def close_box():
    write_config("testaa", "oopenn")
    print('Hello world!')
    os.system("~/close_box.py")
    return "Box close script called"


@app.route("/set-time")
def set_open_time():
    write_config("open_time", request.args.get('open'))
    write_config("close_time", request.args.get('close'))
    print(request.args.get('open'))
    print(request.args.get('close'))
    return "Set box open time script called"
