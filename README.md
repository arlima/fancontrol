# fancontrol
Controling a 5v fan for raspberry pi

I have a case for raspberry with a 5v (0.2A) fan. Usually is connected to the raspberry ports 4 (5V) and 6 (GND). However, the fan runs all the time. 

In this project I wrote a very simple python code that monitors the raspberry temperature and send signals through the pin 7 (GPIO4) to control a very simple external cirtuit. In the circuit I use a bc 337 transistor and a 1k resistor turn on or off the current from pin 4 to 6.

