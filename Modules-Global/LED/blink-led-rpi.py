#Author: Jesimar da Silva Arantes
#Date: 29/03/2018
#Last Update: 07/11/2018
#Description: Code that blink the led. 
#Descricao: Codigo que pisca o led.

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

pin = int(sys.argv[1]) # sends the signal (pin 36 - called too BCM16)
delay = float(sys.argv[2]) # delay time between blink

GPIO.setup(pin, GPIO.OUT)

while True:
	GPIO.output(pin, GPIO.HIGH)
	time.sleep(delay)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(delay)
