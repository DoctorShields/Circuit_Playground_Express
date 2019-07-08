import time
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.3

while True:
    touched = False
    if cpx.touch_A1:
        print("Touched A1!")
        cpx.pixels[6] = (255, 0, 0)
        cpx.start_tone(200)
        touched = True
    if cpx.touch_A2:
        print("Touched A2!")
        cpx.pixels[8] = (210, 45, 0)
        cpx.start_tone(300)
        touched = True
    if cpx.touch_A3:
        print("Touched A3!")
        cpx.pixels[9] = (155, 100, 0)
        cpx.start_tone(400)
        touched = True
    if cpx.touch_A4:
        print("Touched A4!")
        cpx.pixels[0] = (0, 255, 0)
        cpx.start_tone(500)
        touched = True
    if cpx.touch_A5:
        print("Touched A5!")
        cpx.pixels[1] = (0, 135, 125)
        cpx.start_tone(600)
        touched = True
    if cpx.touch_A6:
        print("Touched A6!")
        cpx.pixels[3] = (0, 0, 255)
        cpx.start_tone(700)
        touched = True
    if cpx.touch_A7:
        print("Touched A7!")
        cpx.pixels[4] = (100, 0, 155)
        cpx.start_tone(800)
        touched = True
    if not touched:
        cpx.pixels.fill((0, 0, 0))
        cpx.stop_tone()
    time.sleep(0.1)
