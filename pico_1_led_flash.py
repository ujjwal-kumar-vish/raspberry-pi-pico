
'''
from machine import Pin, Timer

led = machine.Pin("LED", machine.Pin.OUT)
LED_state = True
tim = Timer()

def tick(timer):
    global led, LED_state
    LED_state = not LED_state
    led.value(LED_state)

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)'''

from machine import Pin, Timer

led1 = Pin("LED", machine.Pin.OUT)
led2 = Pin(12,Pin.OUT)

LED_state2 = False
LED_state1 = True

tim = Timer()

def tick(timer):
    global led1, led2, LED_state1, LED_state2
    LED_state1 = not LED_state1
    LED_state2 = not LED_state2
    led1.value(LED_state1)
    led2.value(LED_state2)

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)