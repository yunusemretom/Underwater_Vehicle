import RPi.GPIO as GPIO
import time
from pymavlink import mavutil
import buzzer

master = mavutil.mavlink_connection('udpin:localhost:14550')
master.wait_heartbeat()

buzzer.BUZZER()
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return
    
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)
    
set_rc_channel_pwm(2, pwm=1500)
set_rc_channel_pwm(3, pwm=1500)
set_rc_channel_pwm(4, pwm=1500)
set_rc_channel_pwm(5, pwm=1500)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 24
ECHO = 23

print("HC-SR04 mesafe sensoru")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:

    GPIO.output(TRIG, False)
    print("Olculuyor...")
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print(distance)
    if distance <= 30:
        set_rc_channel_pwm(3, pwm=1400)
    else:
        set_rc_channel_pwm(3 ,pwm=1560)
         
     
