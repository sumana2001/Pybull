import cv2
cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
count = 0
#count = 1
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    NumberPlates = cascade.detectMultiScale(gray, 1.2, 4)
    for(x, y, w, h) in NumberPlates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        #text = "NUMBER PLATE " + str(count)
        cv2.putText(frame, "number plate", (x, y+h+20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
        cropped = frame[y:y+h, x:x+w]
        #s = "NUMPLATE"+ str(count)
        cv2.imshow("number plate", cropped)
        count = count + 1
    cv2.imshow("Live Feed", frame)
    cv2.waitKey(1)

