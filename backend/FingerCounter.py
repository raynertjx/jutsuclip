import cv2
import os
import HandTrackingModule as htm

img = cv2.imread('0Left.jpg')

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]


img = detector.findHands(img)
lmList = detector.findPosition(img, draw=False)
#print(lmList)



handType = detector.findHandType(img)

if len(lmList) != 0 and handType is not None:
    fingers = []
    # Thumb
    print(handType)
    if handType == 'Right':
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
    
    elif handType == 'Left':
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    # 4 Fingers
    for id in range(1, 5):
        if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
            fingers.append(1)
        else:
            fingers.append(0)

    #print(fingers)
    totalFingers = fingers.count(1)
    print(totalFingers)

cv2.imshow("Image", img)
cv2.waitKey(0)
