from Sandbox import KeyPressModule as kp
from djitellopy import tello
from time import sleep

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# --------------------- above is boiler plate ------------------


# initialize the pygame window (make sure it is active to get key presses)qq
kp.init()

while True:
    vals = kp.getKeyboardInput(me)
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)


