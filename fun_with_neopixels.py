from time import sleep
from random import randint
from adafruit_circuitplayground.express import cpx

print("red")
for pixel in range(0,10):
    cpx.pixels[pixel] = (10, 0, 0)
    sleep(.1)
print("green")
for pixel in range(0,10):
    cpx.pixels[pixel] = (0, 10, 0)
    sleep(.1)
print("blue")
for pixel in range(0,10):
    cpx.pixels[pixel] = (0, 0, 10)
    sleep(.1)
print("random")
for pixel in range(0,10):
    cpx.pixels[pixel] = (randint(0,50),randint(0,50),randint(0,50))
    sleep(.1)
print("sparkle")
for i in range(0,100):
    onLed = randint(0,9)
    for pixel in range(0,10):
        if(pixel == onLed):
            cpx.pixels[randint(0,9)] = (100,100,100)
        else:
            cpx.pixels[randint(0,9)] = (0,0,0)
    sleep(.1)

