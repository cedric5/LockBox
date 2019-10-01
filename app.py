from flask import Flask, render_template

app = Flask(__name__)
import subprocess
import os
import datetime
import time


def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered


@app.route("/")
def show_main_page():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'content': render_page("status",{'box_status': 'open', 'open_close_time': '10-07-2019 - 18:00'})
    }
    return render_template('main.html', **templateData)


def render_status_page():
    templateData = {
        'box_status': 'closed',
    }
    renderd = render_template('status.html', **templateData)
    return renderd


@app.route("/wifi")
def show_wifi_page():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    content_html = open("templates/wifi-settings.html").read()
    templateData = {
        'title': 'HELLO!',
        'time': timeString,
        'content': content_html
    }
    return render_template('main.html', **templateData)


@app.route("/reboot")
def show_reboot_page():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    content_html = open("templates/reboot.html").read()
    templateData = {
        'title': 'HELLO!',
        'time': timeString,
        'content': content_html
    }
    return render_template('main.html', **templateData)


@app.route("/open-close")
def open_close():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    content_html = open("templates/open-close-settings.html").read()
    templateData = {
        'title': 'HELLO!',
        'time': timeString,
        'content': content_html
    }
    return render_template('main.html', **templateData)


@app.route("/open-box")
def open_box():
    os.system("~/open_box.py")
    return "Box open script called"


@app.route("/close-box")
def close_box():
    os.system("~/close_box.py")
    return "Box close script called"


@app.route("/set-close-time")
def set_close_time():
    return "Set box close time script called"


@app.route("/set-open-time")
def set_open_time():
    return "Set box open time script called"
