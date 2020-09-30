# to take video as input
cap = cv2.VideoCapture("Resources/hattbe.mp4")

# video is a sequence of pictures so we capture photos step by step and display it
while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    # looks into delay and q press and exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break