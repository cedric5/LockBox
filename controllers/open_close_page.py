import tools
from flask import Flask, render_template
from flask import request


def show():

    content_html = open("templates/open-close-settings.html").read()
    template_data = {
        'content': tools.render_page("open-close-settings",
                                     {"open_time": tools.get_config('open_time'),
                                      "close_time": tools.get_config("close_time"),
                                      "box_status": tools.get_config("box_status"),
                                      "alert": alert()[1],
                                      "alert_type": alert()[0],
                                      "mode": tools.get_config("mode")
                                      })
    }
    return render_template('main.html', **template_data)


def alert():
    if tools.get_config('box_status') == "closed" and tools.get_config('mode') == 'automatic':
        return "danger", "The box is closed, you can not change these settings until the box opens at the set time"
    else:
        return "", ""
