#!/usr/bin/python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if(GPIO.input(17) ==1):
	print('NO')
else:
	print('YES')
GPIO.cleanup()

