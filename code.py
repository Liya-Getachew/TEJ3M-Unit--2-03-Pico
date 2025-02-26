"""
Created by Liya G. on Feb. 26 2025
This makes the LED blink every second using a breadboard.
The blink time increments by 1 every loop.
"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

blink_time = 1

# loop forever
while True:
    print(blink_time)
    led.value = True # turns LED on
    time.sleep(blink_time) # wait for 1000ms
    led.value = False # turns LED off
    time.sleep(blink_time) # wait for 1000ms

    blink_time += 1 # add one second to blink_time every loop
