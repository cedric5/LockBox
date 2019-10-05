import pigpio
from time import sleep

# connect to the
pi = pigpio.pi()

print("closing box")
pi.set_servo_pulsewidth(23, 1700)  # middle
sleep(1)
pi.set_servo_pulsewidth(23, 0)
