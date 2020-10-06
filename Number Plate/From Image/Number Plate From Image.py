import cv2
import numpy as np

cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
count = 1
frame = cv2.imread('im3.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
NumberPlates = cascade.detectMultiScale(gray, 1.1, 4)
window_W, window_H = 1000, 600
window = np.zeros([window_H, window_W,3], np.uint8)
cx, cy = 0, 0
Window_text = "NUMBER PLATES"
cv2.putText(window, Window_text, (405, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
for(x, y, w, h) in NumberPlates:
    cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    text = "NUMBER PLATE " + str(count)
    cv2.putText(frame, text, (x, y+h+20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
    cropped = frame[y+2:y+h-2, x+2:x+w-2]
    s = "NUMPLATE"+ str(count)
    #cv2.imshow(s, cropped)
    count = count + 1
    ch,cw, _ = cropped.shape
    #print(ch)
    #print(cw)
    window_X, window_Y = int((window_W-cw)/2), int((window_H-ch)/2)+cy
    window_X2, window_Y2 = int((window_W+cw)/2), int((window_H+ch)/2)+cy
    window[window_Y:window_Y2, window_X:window_X2] = cropped
    cv2.rectangle(window, (window_X, window_Y), (window_X+cw, window_Y+ch), (255, 255, 255), 2)
    cy = cy + ch + 10
    #cx = cx + cw
cv2.imshow("window", window)
cv2.imshow("Live Feed", frame)
cv2.waitKey(1)
#cv2.destroyAllWindows()

