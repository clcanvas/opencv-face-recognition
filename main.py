import cv2
import numpy as np
#import face_recognition

capture = cv2.VideoCapture("hello.mp4")

# use training data for face in frame

while True:
    ret, frame = capture.read()

    # use face positions to create rectangle each frame 
    frame = cv2.rectangle(frame, (800, 200), (1200,600), (255, 255, 255), 10)

    # show the edited frame
    cv2.imshow('Video', frame)

    # quit the program
    if cv2.waitKey(1) == ord("q"):
        break