import pigpio
import tools
from time import sleep


def open_box():
    print("opening box: unlocking")
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(17, 2225)
    sleep(0.2)
    pi.set_servo_pulsewidth(17, 0)
    print("opening box: opening lid")
    pi.set_servo_pulsewidth(23, 1725)
    sleep(0.1)
    tools.write_config("box_status", "open")


def close_box():
    print("closing box: closing lid")
    pi = pigpio.pi()
    pulse = 1725  # open position of lid
    while pulse < 1150:  # 1100 close position of lid
        pulse -= 25
        print(pulse)
        pi.set_servo_pulsewidth(23, pulse)
        sleep(0.05)
    pi.set_servo_pulsewidth(23, 0)
    print("closing box: locking")
    pi.set_servo_pulsewidth(17, 2000)
    sleep(0.1)
    pi.set_servo_pulsewidth(17, 0)
    tools.write_config("box_status", "closed")
