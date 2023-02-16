import cv2
import numpy as np

lower = np.array([20, 150, 20])
upper = np.array([35, 255, 255]) # jugador
#lower = np.array([0, 130, 20])
#upper = np.array([20, 255, 255])# ENEMIGOS,


img = cv2.imread("hey.png")

while True:
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)

    cv2.imshow("mask", mask)
    cv2.imshow("webcam", img)

    cv2.waitKey()