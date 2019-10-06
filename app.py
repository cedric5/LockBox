import json
import os
import tools as tools
import timer as timer
from flask import Flask
from flask import request


import controllers.wifi_page as wifi_page_controller
import controllers.open_close_page as open_close_page_controller
import controllers.reboot_page as reboot_page_controller
import controllers.status_page as status_page_controller

app = Flask(__name__)

def render_page(page, page_data):
    rendered = render_template(page + '.html', **page_data)
    return rendered

@app.route("/")
def show_main_page():
 return status_page_controller.show()

@app.route("/wifi")
def show_wifi_page():
    return wifi_page_controller.show()


@app.route("/reboot")
def show_reboot_page():
    return reboot_page_controller.show()


@app.route("/reboot-device-loader")
def show_reboot_device_page():
    return render_template("wait-for-reboot.html")


@app.route("/reboot-device")
def reboot_device():
    os.system("sudo reboot")
    print('rebooting')
    return "rebooting"


@app.route("/open-close")
def show_open_close_page():
    return open_close_page_controller.show()

@app.route("/open-box")
def open_box():
    tools.open_box()
    return "Box open script called"


@app.route("/close-box")
def close_box():
    tools.close_box()
    return "Box close script called"


@app.route("/set-time")
def set_times():
    if tools.get_config("box_status") == "open":
        tools.write_config("open_time", request.args.get('open'))
        tools.write_config("close_time", request.args.get('close'))
        return "Open/closing times are set!"
    else:
        return "The box is closed! You can not change these settings now"


@app.route("/set-wifi")
def set_wifi():
    tools.write_config("wifi_ssid", request.args.get('wifi_ssid'))
    tools.write_config("wpa2", request.args.get('wpa2'))
    return "Set wifi settings saved!"

timer.start_timer()
