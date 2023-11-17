import RPi.GPIO as GPIO
import time


def BUZZER(sure=3):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    buzzer = 12


    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.output(buzzer, False)
    print("ÖTÜYOR")
    time.sleep(0.1)

    GPIO.output(buzzer, True)
    time.sleep(sure)
    GPIO.output(buzzer, False)

