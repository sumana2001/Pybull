import cv2

img = cv2.imread('Resources/me.jpeg')

# display img but does immediately so we add delay, 0 means infinite delay rest in 'ms'
cv2.imshow('Output',img)
cv2.waitKey(0)