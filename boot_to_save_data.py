import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.D7) # this is the switch 
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# switch to the left means your computer can write to the CPX
# switch to the right means CircuitPython can save data to the CPX
storage.remount("/", switch.value)
