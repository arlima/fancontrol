#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import signal
import sys

def handleTERM(signal, frame):
    print('Stopping...')
    p.stop()
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handleTERM)
signal.signal(signal.SIGTERM, handleTERM)
signal.signal(signal.SIGHUP, handleTERM)


pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
p = GPIO.PWM(pin, 100)
p.start(0)
temp_max = 60.0
temp_min = 35.0
dc_min = 20
dc_max = 100
temp = 0.0

while True:
	f = open ('/sys/class/thermal/thermal_zone0/temp','r')
	r = f.readline()
	#print (r)
	temp = float(r)/1000.0
	#print(temp)
	if temp > temp_max:
		dc = dc_max
	elif temp < temp_min:
		dc = dc_min
	else:
		dc = (1-(temp_max - temp)/(temp_max - temp_min))*(dc_max-dc_min)+dc_min
	#print(temp,',', dc)
	p.ChangeDutyCycle(dc)
	f.close()
	time.sleep(1)

p.stop()
GPIO.cleanup()
