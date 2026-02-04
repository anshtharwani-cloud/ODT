from machine import Pin
import time
pb_1 = Pin(33, Pin.IN,Pin.PULL_UP)
astro = Pin(18, Pin.OUT)
while True:
    astro.on()
    time.sleep(0.25)
    astro.off()
    time.sleep(0.75)