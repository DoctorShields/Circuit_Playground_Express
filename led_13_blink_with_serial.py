import time
from adafruit_circuitplayground.express import cpx
 
while True:
    print("led on")
    cpx.red_led = True
    time.sleep(0.5)
    print("led off")
    cpx.red_led = False
    time.sleep(0.5)
