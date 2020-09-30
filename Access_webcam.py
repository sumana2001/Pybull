import cv2

# to access the webcam
# 0 is the id of the webcam if more than 1 webcam you can select from index
cap = cv2.VideoCapture(0)
cap.set(3,640)  # width is id 3
cap.set(4,480)  # height is id 4
cap.set(10,100) # brightness id 10

while True:
    success , img = cap.read()
    cv2.imshow("Webcam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
