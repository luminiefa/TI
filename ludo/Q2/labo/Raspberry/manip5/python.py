#!/usr/bin/en python

import serial
import time

portUSB = '/dev/ttyACM0'

try:
    ser=serial.Serial(portUSB, baudrate=9600)

    while True:
        ligne=ser.readline()
        print(ligne.decode('utf-8'))

except Exception as e:
    print(e)