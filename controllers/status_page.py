import tools
from flask import Flask, render_template
from flask import request

def show():


    open_time = tools.get_config("open_time")
    close_time = tools.get_config("close_time")
    wifi_ssid = tools.get_config("wifi_ssid")
    wifi_strength = tools.get_config("wifi_strength")
    time_left_arr = tools.time_left(box_status)
    mode = tools.get_config("mode")
    template_data = {
        'content': tools.render_page("status",
                               {'box_status': box_status(),
                                "future_box_status": future_box_status(),
                                'open_time': open_time,
                                "close_time": close_time,
                                "time_left": time_left_arr,
                                "wifi_ssid": wifi_ssid,
                                "mode": mode})
    }

    return render_template('main.html', **template_data)

def future_box_status():
    box_status = tools.get_config("box_status")
    if box_status == "closed":
        return 'open'
    else:
        return "close"

def box_status():
    return tools.get_config("box_status")
