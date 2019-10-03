import json
from datetime import date
from flask import Flask, render_template
from flask import request
from dateutil import relativedelta
import pdb
from datetime import datetime, time
from time import sleep
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


def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days * 24 * 3600 + timedelta.seconds


def daysHoursMinutesSecondsFromSeconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours, minutes, seconds)


def time_left(box_status):
    if box_status == "closed": open_close_time = get_config('open_time')
    if box_status == "open": open_close_time = get_config('close_time')

    time_to_compare = datetime.datetime.strptime(open_close_time, '%Y-%m-%d %H:%M')
    now = datetime.datetime.now()
    return daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, time_to_compare))


@app.route("/")
def show_main_page():
    box_status = get_config("box_status")
    if box_status == "closed":
        future_box_status = 'open'
    else:
        future_box_status = "close"

    open_time = get_config("open_time")
    close_time = get_config("close_time")
    wifi_ssid = get_config("wifi_ssid")
    wifi_strength = get_config("wifi_strength")
    time_left_arr = time_left(box_status)
    print(time_left_arr)

    template_data = {
        'content': render_page("status",
                               {'box_status': box_status,
                                "future_box_status": future_box_status,
                                'open_time': open_time,
                                "close_time": close_time,
                                "time_left": time_left_arr,
                                "wifi_ssid": wifi_ssid})
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
@app.route("/reboot-device")
def reboot_device():
    os.system("reboot")
    return render_template("wait-for-reboot.html")


@app.route("/open-close")
def show_open_close_page():
    alert = open_close_page_alert()
    content_html = open("templates/open-close-settings.html").read()
    template_data = {
        'content': render_page("open-close-settings",
                               {"open_time": get_config('open_time'),
                                "close_time": get_config("close_time"),
                                "box_status": get_config("box_status"),
                                "alert": alert[1],
                                "alert_type": alert[0]
                                })
    }
    return render_template('main.html', **template_data)


def open_close_page_alert():
    if get_config('box_status') == "closed":
        return "danger", "The box is closed, you can not change these settings until the box opens at the set time"
    else:
        return "", ""


@app.route("/open-box")
def open_box():
    os.system("~/open_box.py")
    write_config("box_status", "open")
    return "Box open script called"


@app.route("/close-box")
def close_box():
    os.system("~/close_box.py")
    write_config("box_status", "closed")
    return "Box close script called"


@app.route("/set-time")
def set_open_time():
    if get_config("box_status") == "open":
        write_config("open_time", request.args.get('open'))
        write_config("close_time", request.args.get('close'))
        return "Open/closing times are set!"
    else:
        return "The box is closed! You can not change these settings now"


@app.route("/set-wifi")
def set_wifi():
    write_config("wifi_ssid", request.args.get('wifi_ssid'))
    write_config("wpa2", request.args.get('wpa2'))
    return "Set wifi settings saved!"
