import cv2
import numpy as np
import PIL
import time
import matplotlib.pyplot as plt
import imutils
import math

# get camera
cap1 = cv2.VideoCapture(0)
# cap2 = cv2.VideoCapture('cam2.mp4')


start_time = time.time()


point_time1 = []
point_time2 = []

point_blue_x = []
point_blue_y = []

point_red_x = []
point_red_y = []

point_red_x2 = []
point_red_y2= []



x_medium = 0
y_medium = 0
M = []
Distance = []
dis = []

cx1 = 0
cy1 = 0
cx2 = 0
cy2 = 0
# cx3 = 0
# cy3 = 0

point_cx1 = []
point_cy1 = []
point_cx2 = []
point_cy2 = []

while (cap1.isOpened()):


    ret, frame = cap1.read()
    if ret == False:
        break
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    current_time = time.time() # set start time


## Contour Object
    # red color
    low_red = np.array([0, 100, 120])
    high_red = np.array([10, 255, 255])

    #blue color
    low_blue = np.array([0, 100, 120])
    high_blue = np.array([90, 255, 255])

    #set mask blue and red
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)



    # contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    cnt_red = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt_red = imutils.grab_contours(cnt_red)

    cnt_blue = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt_blue = imutils.grab_contours(cnt_blue)


    # for cnt in contours:
    #     (x, y, w, h) = cv2.boundingRect(cnt)
    #
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     x_medium = int((x + x + w) / 2)
    #     y_medium = int((y + y + h) / 2)
    #     # point.append(x_medium)
    #
    #     break

# find contour of red
    for c in cnt_red:
        area1 = cv2.contourArea(c)

        if area1 > 5000:

            cv2.drawContours(frame,[c],-1,(0, 255, 0), 3)

            M = cv2.moments(c)

            cx1 = int(M["m10"]/ M["m00"])
            cy1 = int(M["m01"]/ M["m00"])

            cv2.circle(frame, (cx1, cy1), 7, (255, 255, 255), -1)

            # if area1 == 0:
            #     cx1 = 0
            #     cy1 = 0

    point_cx1.append(cx1)
    point_cy1.append(cy1)
    print("cx1 :", cx1)
    print("cy1: ", cy1)
        # if area1 == None:
        #     cx1 = 0
        #     cy1 = 0
        #     point_cx1.append(cx1)
        #     point_cy1.append(cy1)
        #     print("cx1 :", cx1)
        #     print("cy1: ", cy1)

    # find contour of blue
    for c in cnt_blue:
        area2 = cv2.contourArea(c)

        if area2 > 5000:
            # cx2 = 0
            # cy2 = 0

            cv2.drawContours(frame,[c],-1,(0, 255, 0), 3)

            M = cv2.moments(c)

            cx2 = int(M["m10"]/ M["m00"])
            cy2 = int(M["m01"]/ M["m00"])

            cv2.circle(frame, (cx2, cy2), 7, (255, 255, 255), -1)
            # if area2 ==  0:
            #     cx2 = 0
            #     cy2 = 0
    point_cx2.append(cx2)
    point_cy2.append(cy2)
    print("cx2 :", cx2)
    print("cy2: ", cy2)

        # if area2 == None:
        #     cx2 = 0
        #     cy2 = 0
        #     point_cx2.append(cx2)
        #     point_cy2.append(cy2)
        #     print("cx2 :", cx2)
        #     print("cy2: ", cy2)


# append value
    elapsed_time1 = current_time - start_time
    # dis = math.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)
    # Distance.append(dis)
    # point_time1.append(elapsed_time1)
    # point_blue_x.append(cx2)
    # point_blue_y.append(cy2)
    # point_red_x.append(cx1)
    # point_red_y.append(cy1)




    cv2.imshow("Frame", frame)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap1.release()

#############################################################################################################################
### Camera 2 ###

# while(cap2.isOpened()):
#     ret2, frame2 = cap2.read()
#     if ret2 == False:
#         break
#
#     hsv_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
#     current_time = time.time()  # set start time
#
#     low_yel2 = np.array([25, 70, 120])
#     high_yel2 = np.array([30, 255, 255])
#     red_mask2 = cv2.inRange(hsv_frame2, low_yel2, high_yel2)
#     cnt_yel2 = cv2.findContours(red_mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cnt_yel2 = imutils.grab_contours(cnt_yel2)
#
#     for c in cnt_yel2:
#         area3 = cv2.contourArea(c)
#         if area3 > 1000:
#
#             cv2.drawContours(frame2,[c],-1,(0, 255, 0), 3)
#
#             M = cv2.moments(c)
#
#             cx3 = int(M["m10"]/ M["m00"])
#             cy3 = int(M["m01"]/ M["m00"])
#
#             cv2.circle(frame2, (cx1, cy1), 7, (255, 255, 255), -1)
#
#         if area3 < 1000:
#             cx1 = 0
#             cy1 = 0
#
#     elapsed_time2 = current_time - start_time
#     point_time2.append(elapsed_time2)
#
#
#     point_red_x2.append(cx3)
#     point_red_y2.append(cy3)
#
#     cv2.imshow("Frame", frame2)
#
#     key = cv2.waitKey(1)

    # if key == ord("q"):
    #     break


# cap2.release()
cv2.destroyAllWindows()






# plot distance in each array

# for i in range(1, len(point_red_x)):
#      Distance[i] = math.sqrt((point_blue_x[i] - point_red_x[i]) ** 2 + (point_blue_y[i] - point_red_y2[i]) ** 2)


# print value of array

# print("point:blue_x" , point_blue_x)
# print("length of blue_x: ", len(point_blue_x))
# print("point:blue_y" , point_blue_y)
# print("length of blue_ั: ", len(point_blue_y))
# print("point red_x:" , point_red_x)
# print("length of red_x: ", len(point_red_x))
# print("point red_y:", point_red_y2)
# print("length of red_y: ", len(point_red_y))
# print("point time: " , point_time1)
# print("length of point time: ", len(point_time1))
# print("Distance : ", Distance)


print("point red_x" , point_cx1)
print("length of red_x: ", len(point_cx1))
print("point red_y" , point_cy1)
print("length of red_y_ั: ", len(point_cy1))
print("point red_x:" , point_cx2)
print("length of blue_x: ", len(point_cx2))
print("point red_y:", point_cy2)
print("length of blue_y: ", len(point_cy2))

# plot distance and time
plt.plot(point_time1, Distance)
plt.show()