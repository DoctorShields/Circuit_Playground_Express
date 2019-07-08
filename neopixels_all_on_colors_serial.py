import time
from adafruit_circuitplayground.express import cpx

print("red")
cpx.pixels.fill((10, 0, 0))
time.sleep(1)
print("green")
cpx.pixels.fill((0, 10, 0))
time.sleep(1)
print("blue")
cpx.pixels.fill((0, 0, 10))
time.sleep(1)
print("white")
cpx.pixels.fill((10, 10, 10))
time.sleep(1)
print("off")
cpx.pixels.fill((0, 0, 0))
time.sleep(1)
