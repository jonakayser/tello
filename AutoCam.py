from djitellopy import tello
from time import sleep
import cv2

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# --------------------- above is boiler plate ------------------

# start video stream
me.streamon()

# take-off
print("Take-off")
me.takeoff()
sleep(5)

#me.move_down(35)

# fly a pattern
speed = 15
distance = 70

me.go_xyz_speed(-(distance-10), 0, 0, speed)

for wp in range(4):
    me.go_xyz_speed(distance,distance,0,speed)
    me.rotate_clockwise(90)
    print('arriving at waypoint:{}'.format(wp+1))
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))    # resize for better processing speed
    cv2.imwrite(str(wp)+'.png',img)



# land
me.streamoff()
me.land()
me.end()
