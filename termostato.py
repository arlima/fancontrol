#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import signal
import sys

def handleTERM(signal, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handleTERM)

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)

while True:
	f = open ('/sys/class/thermal/thermal_zone0/temp','r')
	r = f.readline()
	#print (r)
	temp = float(r)/1000.0
	#print(temp)
	if temp > 55.0:
		GPIO.output(pin,GPIO.HIGH)
		#print('Temperature is', temp, '. Fan is ON')
	if temp < 45.0:
		GPIO.output(pin,GPIO.LOW)
		#print('Temperature is', temp, '. Fan is OFF')
	f.close()
	time.sleep(10)

GPIO.cleanup()
