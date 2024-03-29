import cv2
import HandTrackingModule as htm
import pyperclip
import os
import time

current, previous = "", ""

def finger_tracker(stored_values):
    def capture_video():
        global current
        global previous
        wCam, hCam = 640, 480

        cap = cv2.VideoCapture(0)
        cap.set(3, wCam)
        cap.set(4, hCam)

        detector = htm.handDetector(detectionCon=0.75)

        tipIds = [4, 8, 12, 16, 20]

        startTime = None

        while True:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
            # print(lmList)
            handType = detector.findHandType(img)

            if len(lmList) != 0:
                fingers = []

                if handType == "Right":
                    if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                elif handType == "Left":
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

                # print(fingers)
                totalFingers = fingers.count(1)
                stored_value = stored_values[totalFingers]

                if current != stored_value:
                    if startTime is None:
                        startTime = time.time()  # Start the timer
                    elif time.time() - startTime >= 1:  # Check if 2 seconds have passed
                        previous = current
                        current = stored_value
                        os.system(f"osascript -e 'display notification \"Current Copy: {current}\"'")
                        pyperclip.copy(stored_value)
                        print(stored_value)
                else:
                    startTime = None  # Reset the timer if the gesture is the same

            cv2.imshow("Image", img)
            cv2.waitKey(1)

    return capture_video
