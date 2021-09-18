import tellopy
import av
import cv2
import numpy

drone = tellopy.Tello()
drone.connect()

print('START Video thread')
drone.start_video()
container = av.open(drone.get_video_stream())
print('Go!')
while True:
    for frame in container.decode(video=0):
        image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
        #image = cv2.resize(image, (720, 480))


        cv2.imshow('Original', image)
        cv2.waitKey()

cv2.destroyWindow('Original')


