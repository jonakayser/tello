import cv2

cap = cv2.VideoCapture(2)

while True:
    _, img = cap.read()
    cv2.imshow("Output", img)

    cv2.waitKey(1)