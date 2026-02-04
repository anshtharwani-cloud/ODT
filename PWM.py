from machine import Pin,PWM
import time
ir = Pin(13, Pin.IN,Pin.PULL_UP)
astro = PWM(Pin(18))
astro.freq(1000)

while True:
    ir = ir.value()
    if ir == 0:
        for p in range(0,1023,10):
            astro.duty(p)
            time.sleep(0.01)
        for p in range(1023,0,-10): 
            astro.duty(p)
            time.sleep(0.01)

        
