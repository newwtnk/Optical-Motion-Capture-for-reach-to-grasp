import cv2
import mediapipe as mp
import time
import math
import HandTrackingModule as htm
import matplotlib.pyplot as plt

pTime = 0
cTime = 0
distance = []
Time = []
coordinate_1 = []
coordinate_2 = []
cap1 = cv2.VideoCapture('cam1.mp4')
cap2 = cv2.VideoCapture('cam2.mp4')

detector = htm.handDetector()
while True:
    success, img = cap1.read()
    if success == False:
        break

    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]


        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        length = math.hypot(x2 - x1, y2 - y1)
        print(length)

    distance.append(length)
    coordinate_1.append([x1,y1])
    coordinate_2.append([x2,y2])



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    Time.append(pTime)

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

cap1.release()
cv2.destroyAllWindows()

print(distance)
print("length of distance : ", len(distance))
print(Time)
print("length of Time : ", len(Time))
print("Coordinate of point 1", coordinate_1)
print("Coordinate of point 2", coordinate_2)


plt.plot(Time, distance)
plt.show()