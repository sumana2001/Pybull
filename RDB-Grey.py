import cv2
img = cv2.imread("Resources/me.jpeg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Grey Image",imgGray)
cv2.waitKey(0)