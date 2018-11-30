#Author: Jesimar da Silva Arantes
#Date: 29/03/2018
#Last Update: 07/11/2018
#Description: Code that open the parachute. 
#Descricao: Codigo que abre o paraquedas. 

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

pin = int(sys.argv[1]) # sends the signal (pin 37 - called too BCM26)

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.HIGH)
