import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

##############
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
##############

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr,hScr)

while True:
    #1. Find handLandmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    #2. get the tip of the index and middle fingers
    if len(lmList)!=0:
        x1,y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print(x1,y1,x2,y2)

        #3. check which fingers are up
        fingers = detector.fingersUp()
        #print(fingers)

        #4. Only index finger : moving Mode
        if fingers[1]==1 and fingers[2]==0:

            #5. Convert Coordinates
            cv2.rectangle(img, (frameR, frameR), (wCam-))
            x3 = np.interp(x1, (0,wCam), (0,wScr))
            y3 = np.interp(y1, (0,hCam), (0,hScr))
            #6. Smoothen Values
            #7. Move mouse
            #fliped version
                #autopy.mouse.move(wScr-x3, hScr-y3)
            autopy.mouse.move(x3, y3)
            cv2.circle(img,(x1, y1), 15, (255,0,255), cv2.FILLED)
        #8. Both index and middle fingers are up : Clicking Mode
        #9. Find distance between fingers
        #10. Click mouse if distance is short

    #11. Frame Rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (90, 0, 255), 3)

    #12. Display
    cv2.imshow("image", img)
    cv2.waitKey(1)


