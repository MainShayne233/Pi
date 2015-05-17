import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk


def init():
	gpio.setmode(gpio.BOARD)
	gpio.setup(7, gpio.OUT)
	gpio.setup(11, gpio.OUT)
	gpio.setup(13, gpio.OUT)
	gpio.setup(15, gpio.OUT)

def forward(tf):
	gpio.output(7, 0)
	gpio.output(11, 1)
	gpio.output(13, 0)
	gpio.output(15, 1)
	time.sleep(tf)
	gpio.cleanup()

def reverse(tf):
	gpio.output(7, 1)
	gpio.output(11, 0)
	gpio.output(13, 1)
    gpio.output(15, 0)
    time.sleep(tf)
	gpio.cleanup()

def forwardright(tf):
	gpio.output(7, 0)
        gpio.output(11, 1)
        gpio.output(13, 0)
        gpio.output(15, 0)
        time.sleep(tf)
        gpio.cleanup()

def forwardleft(tf):
        gpio.output(7, 0)
        gpio.output(11, 0)
        gpio.output(13, 0)
        gpio.output(15, 1)
        time.sleep(tf)
        gpio.cleanup()

def backwardleft(tf):
        gpio.output(7, 1)
        gpio.output(11, 0)
        gpio.output(13, 0)
        gpio.output(15, 0)
        time.sleep(tf)
        gpio.cleanup()

def backwardright(tf):
        gpio.output(7, 0)
        gpio.output(11, 0)
        gpio.output(13, 1)
        gpio.output(15, 0)
        time.sleep(tf)
        gpio.cleanup()

def key_input(event):
	init()
	print 'Key: ', event.char
	key_press = event.char
	sleep_time = 0.100
	
	if key_press.lower() == 'w':
		forward(sleep_time)
	elif key_press.lower() == 's':
		reverse(sleep_time)
	elif key_press.lower() == 'a':
		forwardleft(sleep_time)
	elif key_press.lower() == 'd':
		forwardright(sleep_time)

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
