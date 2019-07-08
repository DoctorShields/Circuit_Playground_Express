import storage
from adafruit_circuitplayground.express import cpx

# switch to the left means your computer can write to the CPX
# switch to the right means CircuitPython can save data to the CPX
storage.remount("/", cpx.switch)
