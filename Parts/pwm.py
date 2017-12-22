import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup([19,26],GPIO.OUT)
GPIO.output(19,GPIO.LOW)
GPIO.output(26,GPIO.LOW)
pwm = GPIO.PWM(26,1)
pwm.start(50)
time.sleep(5)
GPIO.cleanup()
