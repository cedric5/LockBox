import pigpio
from time import sleep

# connect to the
pi = pigpio.pi()

print("opening box")
pi.set_servo_pulsewidth(23, 2500)  # position clockwise
sleep(1)
pi.set_servo_pulsewidth(23, 0)
