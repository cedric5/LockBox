import tools
from flask import Flask, render_template
from flask import request


def show():
    template_data = {
        'content': tools.render_page("wifi-settings",
                               {'wifi_ssid': tools.get_config('wifi_ssid'), 'wifi_wpa2': tools.get_config('wifi_wpa2')})
    }
    return render_template('main.html', **template_data)

