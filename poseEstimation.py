import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture("assets/pose-2.mp4")
pTime = 0

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (100, 80), cv2.FONT_HERSHEY_PLAIN, 5,
    (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
