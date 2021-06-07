from djitellopy import tello
from time import sleep

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# --------------------- above is boiler plate ------------------

# take-off
me.takeoff()

# fly a pattern
me.send_rc_control(0, 20, 0, 0)
sleep(1)

# land
me.send_rc_control(0, 0, 0, 0)
me.land()
