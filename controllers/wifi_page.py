import tools
from flask import Flask, render_template
from flask import request


def show():
    template_data = {
        'content': tools.render_page("wifi-settings",
                               {
                                'wifi_ssid': tools.get_config('wifi_ssid'),
                                'wifi_wpa2': tools.get_config('wifi_wpa2'),
                                "alert": alert()[1],
                                "alert_type": alert()[0],
                               })
    }
    return render_template('main.html', **template_data)

def alert():
    if  tools.has_internet_connection():
        return ["info", "Your box is not connected to your wifi network please setup you wifi connection below."]
    else:
        return ["", ""]

