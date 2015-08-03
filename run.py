#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

lightPin = 4  # GPIO Pin 18
servoPin = 18 # GPIO Pin 18

GPIO.setmode(GPIO.BCM)

# Setup servo pin status
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 100)
pwm.start(0)

# Setup light sensor pin status
GPIO.setup(lightPin, GPIO.OUT)
GPIO.output(lightPin, GPIO.LOW)
time.sleep(0.5)
GPIO.setup(lightPin, GPIO.IN)

def servo_set(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    
try:
    i = 0
    while True:
        v = GPIO.input(lightPin)
        if (v == GPIO.LOW):
            servo_set(30)
            time.sleep(0.1)
            servo_set(60)
            time.sleep(0.1)
            servo_set(30)
            time.sleep(0.1)
            i = i + 1
            print i
                            
except KeyboardInterrupt:
    pass    
