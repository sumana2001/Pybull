import numpy as np
import cv2

# Uses Read video.py
myVideo = cv2.VideoCapture('Sevilla.mp4')

# Choose 100 random frames
myFrames = myVideo.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=100)

frames = []
for f in myFrames:
    myVideo.set(cv2.CAP_PROP_POS_FRAMES, f)
    ret, frame = myVideo.read()
    frames.append(frame)

# Average of frames
bgFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
cv2.imwrite("Sevilla_background.jpg",bgFrame)

# Uses Readimg.py
cv2.imshow('frame',bgFrame)
cv2.waitKey(0)