import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    _, frame = cap.read()
    print(frame)
    cv.imshow('Colmeia', frame)
    if ord('q') == cv.waitKey(20):
        break

