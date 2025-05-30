from machine import Pin
import time

#set up pin 6 as an input with a pull down resistor
button = Pin(6, Pin.IN, Pin.PULL_DOWN)
led = Pin(12, Pin.OUT)
#led = machine.Pin("LED", machine.Pin.OUT)


while True:
    print(button.value())#reads digital state of the button and print it
    time.sleep(0.1)
    
    #turns on the led if the button is on
    if button.value() == 1:
        led.value(1)
     # turns the led off if it is not   
    else:
        led.value(0)