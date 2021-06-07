import cv2

def
cascPath = "Resources/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


def getFaces(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=8,
        minSize=(100, 100)
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    return faces

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


