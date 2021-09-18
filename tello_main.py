'''
Main script for controlling tello drone
by Jona
'''

# imports
import cv2
import tello_module as tm

# initialize tello
drone = tm.startup()

# initialize joystick
screen = tm.init_joystick()

# run main loop
while True:
    # update video
    tm.update_video(drone)

    # fly the drone
    tm.fly(drone, screen)

cv2.destroyWindow('Original')
