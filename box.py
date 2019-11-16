import pigpio
import tools
from time import sleep


def open_box():
    print("opening box: unlocking")
    pi = pigpio.pi()
    pi.set_servo_pulsewidth(17, 2000)
    sleep(0.2)
    pi.set_servo_pulsewidth(17, 0)
    print("opening box: opening lid")
    pi.set_servo_pulsewidth(23, 1725)
    sleep(0.1)


def close_box():
    pi = pigpio.pi()
    print("closing box: closing lid")
    pi.set_servo_pulsewidth(23, 0)
    pulse = 1725  # open position of lid
    while pulse > 1100:  # 1100 close position of lid
        pulse -= 25
        pi.set_servo_pulsewidth(23, pulse)
        sleep(0.03)
    pi.set_servo_pulsewidth(23, 0)
    print("closing box: locking")
    sleep(0.15)
    pi.set_servo_pulsewidth(17, 2250)
    sleep(1)
    pi.set_servo_pulsewidth(17, 0)
