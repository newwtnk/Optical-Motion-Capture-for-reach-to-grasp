import cv2
import mediapipe as mp
import time
import math
import HandTrackingModule as htm
import matplotlib.pyplot as plt

pTime1 = 0
cTime1 = 0
distance = []
Time1 = []
Time2 = []
coordinate_1 = []
coordinate_2 = []
cap1 = cv2.VideoCapture('cam1.mp4')
cap2 = cv2.VideoCapture('cam2.mp4')

detector = htm.handDetector()
while cap1.isOpened():
    success1, img1 = cap1.read()
    if success1  == False:
        break

    img1 = detector.findHands(img1)

    lmList1 = detector.findPosition(img1)

    if len(lmList1) != 0:
        # print(lmList[4], lmList[8])

        x1_1, y1_1 = lmList1[4][1], lmList1[4][2]
        x2_1, y2_1 = lmList1[8][1], lmList1[8][2]

        cv2.circle(img1, (x1_1, y1_1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img1, (x2_1, y2_1), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img1, (x1_1, y1_1), (x2_1, y2_1), (255, 0, 255), 3)

        length_1 = math.hypot(x2_1 - x1_1, y2_1 - y1_1)
        # print(length_1)
    distance.append(length_1)
    coordinate_1.append([x1_1, y1_1])


    cTime1 = time.time()
    fps = 1 / (cTime1 - pTime1)
    pTime1 = cTime1
    Time1.append(pTime1)

    cv2.putText(img1, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)


    cv2.imshow("Image 1", img1)

    cv2.waitKey(1)

cap1.release()

pTime2 = 0
cTime2 = 0

while cap2.isOpened():
    success2, img2 = cap2.read()
    if success2 == False:
        break

    img1 = detector.findHands(img2)

    lmList2 = detector.findPosition(img2)

    if len(lmList2) != 0:
        # print(lmList[4], lmList[8])

        x1_2, y1_2 = lmList2[0][1], lmList2[0][2]


        cv2.circle(img1, (x1_2, y1_2), 15, (255, 0, 255), cv2.FILLED)


        coordinate_2.append([x1_2, y1_2])

    cTime2 = time.time()
    fps = 1 / (cTime2 - pTime2)
    pTime2 = cTime2
    Time2.append(pTime2)

    cv2.putText(img1, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    cv2.imshow("Image 2", img2)

    cv2.waitKey(1)

cap2.release()

cv2.destroyAllWindows()

print(distance)
print("length of distance : ", len(distance))
print(Time1)
print("length of Time : ", len(Time1))
print(Time2)
print("length of Time : ", len(Time2))

print("Coordinate of point 1", coordinate_1)
print("Coordinate of point 2", coordinate_2)

plt.plot(Time1, distance)
plt.show()