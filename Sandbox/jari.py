from djitellopy import tello
import time

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# --------------------- above is boiler plate ------------------
time.sleep(10)

me.takeoff()
me.move_back(20)
me.rotate_clockwise(100)
me.rotate_counter_clockwise(100)
me.move_up(30)
me.flip_forward()
me.flip_back()
me.move_forward(50)
me.move_back(40)
me.land()