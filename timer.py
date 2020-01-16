import threading
import tools
import datetime
import box


def check_times():
    if tools.config_is_set("open_time") or tools.config_is_set("close_time"):
        tools.write_config('mode', 'automatic')
    else:
        tools.write_config('mode', 'manual')
    box_status = tools.get_config("box_status")
    times = tools.time_left(box_status)
    days = times[0]
    hours = times[1]
    minutes = times[2]
    seconds = times[3]
    time_left_total = days + hours + minutes + seconds
    if time_left_total < 1 or days < 0:
        move_lid(box_status)


def move_lid(box_status):
    if box_status == "closed": open_close_time = tools.get_config('open_time')
    if box_status == "open": open_close_time = tools.get_config('close_time')
    try:
        if is_valid_date(open_close_time):
            print("moving box")
            if box_status == "open":
                box.close_box()
            else:
                box.open_box()
    except:
        print('could not get open or close time, is setting.json still valid?')


def is_valid_date(date):
    if date == "": return False
    if datetime.datetime.now() > datetime.datetime.strptime(date, '%Y-%m-%d %H:%M'):
        return False
    return True


def start_timer():
    threading.Timer(1.0, start_timer).start()
    check_times()
