import KeyPressModule as kp
import cv2
from djitellopy import tello
import numpy as np
import time

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# --------------------- above is boiler plate ------------------


# initialize the pygame window (make sure it is active to get key presses)
kp.init()

# start video stream
me.streamon()

# define globals
global img

# initialize face recognition
cascPath = "Resources/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# initialize yaw direction
yaw_direction = 1

#get first frame
img = me.get_frame_read().frame
frame_xcenter = img.shape[1]//2

while True:

    # capture image
    imsize = (720,480)
    img = me.get_frame_read().frame
    img = cv2.resize(img, imsize)    # resize for better processing speed

    # detect faces

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
        # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    if len(faces) > 0:
        x, y, w, h = faces[0]
        yaw_direction = np.sign((x+w//2)-frame_xcenter)

        if yaw_direction == 1:
            frame_color = (0,255,0)
        else:
            frame_color = (0,0,255)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), frame_color, 2)

    # follow face if key is pressed and only one face is present
    if kp.getKey('f') and len(faces):
        x, y, w, h = faces [0]
        calculated_yaw=int(((x+w/2)-imsize[0]/2)/imsize[0]/2*100)
        yv = int(min(100,calculated_yaw*2))
        me.send_rc_control(0, 0, 0, yv)
    elif kp.getKey('f'):
        yv=int(yaw_direction*100)
        me.send_rc_control(0, 0, 0, yv)
    else:
        # keyboard action
        vals = kp.getKeyboardInput(me)
        me.send_rc_control(vals[0], vals[1], vals[2], vals[3])


    # show image
    cv2.imshow("Image", img)
    cv2.waitKey(1)


