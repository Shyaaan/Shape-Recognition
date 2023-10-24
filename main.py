import numpy as np
import cv2
import random
img = cv2.imread('square.png')
imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret , thrash = cv2.threshold(imgGry, 150, 255, cv2.CHAIN_APPROX_NONE)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#cv2.imshow("grayscale",imgGry)

COLOR = (0,255,0)

for contour in contours:
    approx = cv2.approxPolyDP(contour, .0001 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, COLOR, 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    print(len(approx))
    if len(approx) > 100:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, COLOR)
imgwindow = "the picture"
cv2.namedWindow(imgwindow, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(imgwindow, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE)
cv2.imshow(imgwindow, img)
cv2.waitKey(0)
cv2.destroyAllWindows()