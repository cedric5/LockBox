import tools
from flask import Flask, render_template
from flask import request

def show():
    content_html = open("templates/reboot.html").read()
    template_data = {
        'content': content_html
    }
    return render_template('main.html', **template_data)

def reboot():
    return render_template("wait-for-reboot.html")