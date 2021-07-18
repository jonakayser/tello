from djitellopy import tello
from time import sleep

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# --------------------- above is boiler plate ------------------

# take-off
print("Take-off")
me.takeoff()
sleep(5)

# fly a pattern
speed = 15
for wp in range(4):
    me.go_xyz_speed(30,30,0,speed)
    me.rotate_clockwise(90)
    print('waypoint:{}'.format(wp+1))



# land
me.land()
