from djitellopy import tello
import cv2

# instantiate and connect tello drone
me = tello.Tello()
me.connect()

# get battery status
print(me.get_battery())

# start video stream
me.streamon()
while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))    # resize for better processing speed
    cv2.imshow("Image", img)
    cv2.waitKey(1)
