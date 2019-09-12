#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import zmq


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://*:6001')

reader = SimpleMFRC522()

while True:
    try:
        id, text = reader.read()
        print(id)
        print(text)
        socket.send_string('card', zmq.SNDMORE)
        socket.send_string(str(id))

    finally:
        GPIO.cleanup()
