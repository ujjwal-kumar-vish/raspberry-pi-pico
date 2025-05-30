from machine import Pin
import time

#set up pin 6 as an input with a pull down resistor
button = Pin(6, Pin.IN, Pin.PULL_DOWN)


while True:
    print(button.value())#reads digital state of the button and print it
    time.sleep(0.1)