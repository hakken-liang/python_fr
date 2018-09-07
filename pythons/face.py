# -*- coding: UTF-8 -*-
import numpy as np
import cv2


login="不知是誰"

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite( './faces/' + login + '.jpg',frame)
        break

# When everything done, release the captur
cap.release()
cv2.destroyAllWindows()