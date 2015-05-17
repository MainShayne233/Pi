import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

gpio.output(7, 0)
gpio.output(11, 1)
gpio.output(13, 0)
gpio.output(15, 1)
time.sleep(0.5)

gpio.cleanup()
