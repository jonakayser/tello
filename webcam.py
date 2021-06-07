import cv2
import numpy as np

cascPath = "Resources/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(2)

# initialize yaw direction
yaw_direction = 1

#get first frame
ret, frame = video_capture.read()
frame_xcenter = frame.shape[1]//2

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(100, 100)
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    if len(faces) > 0:
        x, y, w, h = faces[0]
        yaw_direction = np.sign((x+w//2)-frame_xcenter)

        if yaw_direction == 1:
            frame_color = (0,255,0)
        else:
            frame_color = (0,0,255)


    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), frame_color, 2)




    # Display the resulting frame
    cv2.imshow('Video', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
