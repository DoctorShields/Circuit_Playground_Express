import time
from adafruit_circuitplayground.express import cpx

try:
    fn = "/temperature" + str(time.time()) + ".txt"
    with open(fn, "a") as fp:
        while True:
            temp = cpx.temperature
            fp.write('{0:f}\n'.format(temp))
            fp.flush()
            cpx.red_led = not cpx.red_led
            time.sleep(1)
except OSError as e:
    delay = 0.2
    if e.args[0] == 28:
        delay = 0.1
    while True:
        cpx.red_led = not cpx.red_led
        time.sleep(delay)
