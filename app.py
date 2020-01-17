import datetime
import json
import os
import box
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


@app.route("/set-next-friday")
def set_to_next_friday():
    next_friday = tools.get_next_friday()
    tools.write_config("close_time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    tools.write_config("open_time", next_friday.strftime("%Y-%m-%d %H:%M"))
    print(next_friday.strftime("%Y-%m-%d %H:%M"))
    box.close_box()
    return 'date set to next friday!'


@app.route("/reboot")
def show_reboot_page():
    return reboot_page_controller.show()


@app.route("/reboot-device-loader")
def show_reboot_device_page():
    return reboot_page_controller.reboot()


@app.route("/reboot-device")
def reboot_device():
    os.system("python /home/pi/LockBox/scripts/reboot.py")
    print('rebooting')
    return "rebooting"


@app.route("/open-close")
def show_open_close_page():
    return open_close_page_controller.show()


@app.route("/open-box")
def open_box():
    if tools.get_config('mode') == 'automatic':
        print('Box in automatic mode, manual control disabled')
    else:
        box.open_box()
    return "Box open script called"


@app.route("/close-box")
def close_box():
    if tools.get_config('mode') == 'automatic':
        print('Box in automatic mode, manual control disabled')
    else:
        box.close_box()
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


@app.route('/google', methods=['POST'])
def open_box_google():
    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['action']
    if action == 'open-box':
        box.open_box()
    if action == 'close-box':
        box.close_box()
    return action


if not os.path.exists('settings.json'):
    tools.create_settings()
timer.start_timer()
